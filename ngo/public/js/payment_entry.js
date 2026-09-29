frappe.ui.form.on("Payment Entry", {
	refresh: function(frm) {
		if (frm.doc.party_type === "Supplier" && frm.doc.custom_destination === "Donor" && frm.doc.party) {
			fetch_donor_fields(frm);
		}
	},
	party: function(frm) {
		if (frm.doc.party_type === "Supplier" && frm.doc.party) {
			frappe.db.get_value("Supplier", frm.doc.party, "supplier_type").then(function(r) {
				if (r && r.message && r.message.supplier_type) {
					frm.set_value("custom_destination", r.message.supplier_type);
				}
			});
		} else {
			frm.set_value("custom_destination", "");
		}

		if (frm.doc.party_type === "Supplier" && frm.doc.custom_destination === "Donor") {
			fetch_donor_fields(frm);
		} else {
			clear_donor_fields(frm);
		}
	},
	party_type: function(frm) {
		frm.set_value("custom_destination", "");
		clear_donor_fields(frm);
	},
	custom_destination: function(frm) {
		if (frm.doc.party_type === "Supplier" && frm.doc.custom_destination === "Donor") {
			fetch_donor_fields(frm);
		} else {
			clear_donor_fields(frm);
		}
	}
});

function fetch_donor_fields(frm) {
	if (!frm.doc.party) return;

	frappe.db.get_value("Supplier", frm.doc.party, "custom_cost_center", function(r) {
		if (r && r.custom_cost_center) {
			frm.set_value("cost_center", r.custom_cost_center);
		}
	});

	frappe.db.get_value("Project",
		{ "custom_donor": frm.doc.party, "status": "Open" },
		["name", "cost_center"],
		function(proj) {
			if (proj && proj.name) {
				frm.set_value("project", proj.name);
				frappe.db.get_value("Donor Grant",
					{ "linked_project": proj.name, "donor_name": frm.doc.party, "status": "Active" },
					"name",
					function(dg) {
						if (dg && dg.name) {
							frm.set_value("donor_grant", dg.name);
						} else {
							frappe.db.get_value("Donor Grant",
								{ "linked_project": proj.name },
								"name",
								function(dg2) {
									if (dg2 && dg2.name) {
										frm.set_value("donor_grant", dg2.name);
									}
								}
							);
						}
					}
				);
			}
		}
	);
}

function clear_donor_fields(frm) {
	frm.set_value("cost_center", "");
	frm.set_value("project", "");
	frm.set_value("donor_grant", "");
}
