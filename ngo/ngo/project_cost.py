import frappe

def update_project_cost(doc, method=None):
    if doc.docstatus not in (1, 2):
        return
        
    projects = set()
    for row in doc.get('accounts') or []:
        if row.project:
            projects.add(row.project)
            
    if hasattr(doc, 'custom_project') and doc.custom_project:
        projects.add(doc.custom_project)

    for project in projects:
        total_je_expense = frappe.db.sql('''
            SELECT SUM(jea.debit_in_account_currency) - SUM(jea.credit_in_account_currency)
            FROM `tabJournal Entry Account` jea
            JOIN `tabJournal Entry` je ON jea.parent = je.name
            JOIN `tabAccount` acc ON jea.account = acc.name
            WHERE je.docstatus = 1
              AND jea.project = %s
              AND acc.root_type = 'Expense'
        ''', (project,))
        
        total = total_je_expense[0][0] if total_je_expense and total_je_expense[0][0] else 0.0
        
        if frappe.get_meta('Project').has_field('custom_total_expense_via_journal_entry'):
            frappe.db.set_value('Project', project, 'custom_total_expense_via_journal_entry', total)
