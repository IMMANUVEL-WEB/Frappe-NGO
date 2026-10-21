import frappe


NGO_ACCOUNTS = [
    {
        "account_name": "Capital Expenditure",
        "account_type": "",
        "root_type": "Expense",
        "is_group": 0,
        "report_type": "Profit and Loss",
    },
    {
        "account_name": "Admin Expenditure",
        "account_type": "",
        "root_type": "Expense",
        "is_group": 0,
        "report_type": "Profit and Loss",
    },
    {
        "account_name": "Program Expenditure",
        "account_type": "",
        "root_type": "Expense",
        "is_group": 0,
        "report_type": "Profit and Loss",
    },
]


def _get_parent(company, abbr):
    """Return the best parent account name for NGO expense accounts."""
    candidates = [
        "Indirect Expenses - " + abbr,
        "Direct Expenses - " + abbr,
        "Expenses - " + abbr,
    ]
    for candidate in candidates:
        if frappe.db.exists("Account", candidate):
            return candidate
    row = frappe.db.get_value(
        "Account",
        {"company": company, "root_type": "Expense", "is_group": 1},
        "name",
    )
    return row


def execute():
    """
    Idempotently create Capital Expenditure, Admin Expenditure, and
    Program Expenditure accounts for every company on this site.
    Already-existing accounts are silently skipped.
    """
    companies = frappe.get_all("Company", fields=["name", "abbr"])

    for company in companies:
        abbr = company["abbr"]
        company_name = company["name"]
        parent = _get_parent(company_name, abbr)

        if not parent:
            frappe.log_error(
                "ngo/setup_ngo_expense_accounts: Could not find a parent "
                "Expense account for company '{}'. Skipping.".format(company_name),
                "NGO COA Patch",
            )
            continue

        for acct_def in NGO_ACCOUNTS:
            full_name = "{} - {}".format(acct_def["account_name"], abbr)

            if frappe.db.exists("Account", full_name):
                frappe.logger().info(
                    "NGO COA: Account '{}' already exists. Skipping.".format(full_name)
                )
                continue

            acct = frappe.get_doc(
                {
                    "doctype": "Account",
                    "account_name": acct_def["account_name"],
                    "parent_account": parent,
                    "company": company_name,
                    "root_type": acct_def["root_type"],
                    "report_type": acct_def["report_type"],
                    "account_type": acct_def["account_type"],
                    "is_group": acct_def["is_group"],
                }
            )
            acct.insert(ignore_permissions=True)
            frappe.logger().info(
                "NGO COA: Created account '{}' under '{}'.".format(full_name, parent)
            )

    enable_dimensions_in_journal_entry()
    # Ensure Volunteer role does not have home_page override in Role doctype
    if frappe.db.exists("Role", "Volunteer"):
        if frappe.db.get_value("Role", "Volunteer", "home_page"):
            frappe.db.set_value("Role", "Volunteer", "home_page", None)

    frappe.db.commit()


def enable_dimensions_in_journal_entry():
    """Ensure cost center and project accounting dimensions are visible in Journal Entry Account."""
    from frappe.custom.doctype.property_setter.property_setter import make_property_setter

    acc_settings = frappe.get_doc("Accounts Settings")
    if not acc_settings.enable_accounting_dimensions:
        acc_settings.enable_accounting_dimensions = 1
        acc_settings.save(ignore_permissions=True)

    make_property_setter("Journal Entry Account", "accounting_dimensions_section", "hidden", 0, "Check")
    make_property_setter("Journal Entry Account", "accounting_dimensions_section", "collapsible", 0, "Check")
