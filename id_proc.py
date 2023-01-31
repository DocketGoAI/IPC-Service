import json
"""
The script is to make the json dict like, so that we can call with the id
Generates ip_id.json
"""

# Single time running python file
data  = json.load(open('ipc.json', 'r', ))

data = {int(i): item for i, item in enumerate(data)}


with  open('ipc_id.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
