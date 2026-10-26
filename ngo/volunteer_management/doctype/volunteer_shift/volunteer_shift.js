// Copyright (c) 2026, bsoft and contributors
// For license information, please see license.txt

frappe.ui.form.on("Volunteer Shift", {
	refresh(frm) {
		if (!frm.is_new()) {
			frm.add_custom_button(__("create Volunteer attendance"), function () {
				if (frm.is_dirty()) {
					frappe.msgprint(
						__("Please save changes before creating Volunteer Attendance.")
					);
					return;
				}

				const participants = (frm.doc.participants || []).filter((p) => p.volunteer);

				if (participants.length > 1) {
					// Multiple participants: prompt to select which volunteer to mark attendance for
					frappe.prompt(
						[
							{
								fieldname: "volunteer",
								label: __("Select Volunteer"),
								fieldtype: "Select",
								options: participants.map((p) => ({
									value: p.volunteer,
									label: p.volunteer_name
										? `${p.volunteer_name} (${p.volunteer})`
										: p.volunteer,
								})),
								reqd: 1,
								default: participants[0].volunteer,
							},
						],
						function (values) {
							open_new_attendance(frm, values.volunteer);
						},
						__("Select Volunteer for Attendance"),
						__("Proceed")
					);
				} else {
					const vol = participants.length === 1 ? participants[0].volunteer : null;
					open_new_attendance(frm, vol);
				}
			});
		}
	},
});

function open_new_attendance(frm, volunteer) {
	frappe.call({
		method: "ngo.volunteer_management.doctype.volunteer_shift.volunteer_shift.make_volunteer_attendance",
		args: {
			source_name: frm.doc.name,
			volunteer: volunteer || "",
		},
		freeze: true,
		freeze_message: __("Creating Volunteer Attendance..."),
		callback: function (r) {
			if (r.message) {
				var doclist = frappe.model.sync(r.message);
				frappe.set_route("Form", doclist[0].doctype, doclist[0].name);
			}
		},
	});
}
