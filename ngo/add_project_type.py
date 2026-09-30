import frappe

def add_project_type():
    frappe.init(site='ngo.local', sites_path='/home/bsoft/frappe-bench-v16/sites')
    frappe.connect()
    
    # Get current options
    meta = frappe.get_meta("Project")
    field = meta.get_field("project_type")
    
    if not field:
        print("Field project_type not found")
        return
        
    options = field.options or ""
    options_list = [opt.strip() for opt in options.split('\n') if opt.strip()]
    
    if "Donor Project" not in options_list:
        options_list.append("Donor Project")
        
    new_options = '\n'.join(options_list)
    
    frappe.make_property_setter({
        'doctype': 'Project',
        'doctype_or_field': 'DocField',
        'fieldname': 'project_type',
        'property': 'options',
        'value': new_options,
        'property_type': 'Text'
    })
    
    print("Property setter created. New options:", new_options)

    frappe.db.commit()

add_project_type()
