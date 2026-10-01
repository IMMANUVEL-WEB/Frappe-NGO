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
        frm.add_custom_button(__('Make a Journal Entry'), function() {
            frappe.new_doc('Journal Entry', {
                accounts: [
                    { debit_in_account_currency: frm.doc.amount || 0 },
                    { credit_in_account_currency: frm.doc.amount || 0 }
                ]
            });
        }, __('Create'));
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

