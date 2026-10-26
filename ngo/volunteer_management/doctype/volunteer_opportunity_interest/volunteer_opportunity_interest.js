// Copyright (c) 2026, bsoft and contributors
// For license information, please see license.txt

frappe.ui.form.on("Volunteer Opportunity Interest", {
	refresh(frm) {
		if (!frm.is_new()) {
			frm.add_custom_button(__("Create volunteer assignment"), function () {
				if (frm.is_dirty()) {
					frappe.msgprint(
						__("Please save changes before creating a Volunteer Assignment.")
					);
					return;
				}

				if (frm.doc.opportunity) {
					frappe.db.get_value(
						"Volunteer Opportunity",
						frm.doc.opportunity,
						["project", "start_date", "end_date"],
						(r) => {
							frappe.new_doc("Volunteer Assignment", {
								volunteer: frm.doc.volunteer,
								opportunity: frm.doc.opportunity,
								project: r ? r.project : "",
								from_date:
									r && r.start_date ? r.start_date : frappe.datetime.get_today(),
								to_date: r && r.end_date ? r.end_date : "",
								status: "Assigned",
							});
						}
					);
				} else {
					frappe.new_doc("Volunteer Assignment", {
						volunteer: frm.doc.volunteer,
						from_date: frappe.datetime.get_today(),
						status: "Assigned",
					});
				}
			});

			frm.add_custom_button(__("create Volunteer Shift"), function () {
				if (frm.is_dirty()) {
					frappe.msgprint(__("Please save changes before creating a Volunteer Shift."));
					return;
				}

				frappe.call({
					method: "ngo.volunteer_management.doctype.volunteer_opportunity_interest.volunteer_opportunity_interest.make_volunteer_shift",
					args: {
						source_name: frm.doc.name,
					},
					freeze: true,
					freeze_message: __("Creating Volunteer Shift..."),
					callback: function (r) {
						if (r.message) {
							var doclist = frappe.model.sync(r.message);
							frappe.set_route("Form", doclist[0].doctype, doclist[0].name);
						}
					},
				});
			});
		}
	},
});
