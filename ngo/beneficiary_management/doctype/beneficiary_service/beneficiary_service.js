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
