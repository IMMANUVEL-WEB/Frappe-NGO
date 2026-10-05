import frappe

def execute():
    # Mock user session
    frappe.set_user("ravi@gmail.com")
    
    # Import and call API
    from ngo.api.volunteer import open_opportunities
    try:
        opps = open_opportunities()
        print(f"Success! Found {len(opps)} opportunities.")
    except Exception as e:
        print(f"Error: {e}")
