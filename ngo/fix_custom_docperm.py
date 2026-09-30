import json
path = '/home/bsoft/frappe-bench-v16/apps/ngo/ngo/fixtures/custom_docperm.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_data = [d for d in data if d.get('parent') != 'User']

with open(path, 'w', encoding='utf-8') as f:
    json.dump(new_data, f, indent=1)

print(f"Removed User Custom DocPerms. Old count: {len(data)}, New count: {len(new_data)}")
