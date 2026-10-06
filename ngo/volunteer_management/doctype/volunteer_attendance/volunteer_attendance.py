import frappe
from frappe.model.document import Document
from frappe.utils import get_time, time_diff_in_seconds

class VolunteerAttendance(Document):
    def validate(self):
        self.calculate_hours()
        
    def on_update(self):
        self.update_volunteer_hours()
        
    def on_trash(self):
        self.update_volunteer_hours(is_delete=True)
        
    def calculate_hours(self):
        if self.in_time and self.out_time:
            try:
                # time_diff_in_seconds returns difference in seconds between two times/datetimes
                diff = time_diff_in_seconds(self.out_time, self.in_time)
                if diff > 0:
                    self.total_hours = round(diff / 3600.0, 2)
                else:
                    self.total_hours = 0
            except Exception:
                self.total_hours = 0
        
    def update_volunteer_hours(self, is_delete=False):
        if not self.volunteer:
            return
            
        # Calculate total hours for this volunteer
        filters = {"volunteer": self.volunteer}
        if is_delete:
            filters["name"] = ["!=", self.name]
            
        attendances = frappe.get_all("Volunteer Attendance", filters=filters, pluck="total_hours")
        total_hours = sum([float(h or 0) for h in attendances])
        
        frappe.db.set_value("Volunteer", self.volunteer, "total_hours", total_hours)
