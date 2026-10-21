// Copyright (c) 2026, bsoft and contributors
// For license information, please see license.txt

frappe.ui.form.on("Volunteer Assignment", {
	refresh(frm) {
		if (!frm.is_new()) {
			frm.add_custom_button(__("create Volunteer Shift"), function() {
				if (frm.is_dirty()) {
					frappe.msgprint(__("Please save changes before creating a Volunteer Shift."));
					return;
				}

				frappe.call({
					method: "ngo.volunteer_management.doctype.volunteer_assignment.volunteer_assignment.make_volunteer_shift",
					args: {
						source_name: frm.doc.name
					},
					freeze: true,
					freeze_message: __("Creating Volunteer Shift..."),
					callback: function(r) {
						if (r.message) {
							var doclist = frappe.model.sync(r.message);
							frappe.set_route("Form", doclist[0].doctype, doclist[0].name);
						}
					}
				});
			});
		}
	},
});
