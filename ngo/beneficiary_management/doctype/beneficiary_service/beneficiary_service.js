frappe.ui.form.on("Beneficiary Service", {
	setup: function(frm) {
		frm.set_query("enrollment", function() {
			let filters = {
				status: "Active"
			};
			if (frm.doc.beneficiary) {
				filters.beneficiary = frm.doc.beneficiary;
			}
			return {
				filters: filters
			};
		});
	},
	refresh: function(frm) {
		if (!frm.is_new()) {
			frm.add_custom_button(__("Make a Journal Entry"), function() {
				if (frm.is_dirty()) {
					frappe.throw(__("Please save any unsaved changes first before creating a Journal Entry."));
					return;
				}
				frappe.call({
					method: "ngo.beneficiary_management.doctype.beneficiary_service.beneficiary_service.make_journal_entry",
					args: {
						source_name: frm.doc.name
					},
					freeze: true,
					freeze_message: __("Creating Journal Entry..."),
					callback: function(r) {
						if (r.message) {
							var doclist = frappe.model.sync(r.message);
							frappe.set_route("Form", doclist[0].doctype, doclist[0].name);
						}
					}
				});
			}, __("Create"));
		}
	},
	qty: function(frm) {
		calculate_amount(frm);
	},
	rate: function(frm) {
		calculate_amount(frm);
	}
});

function calculate_amount(frm) {
	if (frm.doc.qty && frm.doc.rate) {
		frm.set_value("amount", flt(frm.doc.qty) * flt(frm.doc.rate));
	}
}
