frappe.ui.form.on("Project Proposal", {
	validate: function(frm) {
		calculate_total_budget(frm);
	}
});

frappe.ui.form.on("Budget Item", {
	amount: function(frm, cdt, cdn) {
		calculate_total_budget(frm);
	},
	category: function(frm, cdt, cdn) {
		calculate_total_budget(frm);
	},
	budget_breakdown_remove: function(frm) {
		calculate_total_budget(frm);
	}
});

function calculate_total_budget(frm) {
	let total = 0;
	(frm.doc.budget_breakdown || []).forEach(function(row) {
		total += flt(row.amount);
	});
	frm.set_value("total_budget", total);
}
