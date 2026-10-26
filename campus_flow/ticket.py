from pathlib import Path
import json
JSON_FILE = Path(__file__).resolve().parent / "work_flow.json"


tickets = []
def load_ticket():
    if not JSON_FILE.exists():
        return []
    
    try:
        with open(JSON_FILE, "r") as file:
            data = json.load(file)
            return data if isinstance(data,list) else []
    except (FileNotFoundError, json.JSONDecodeError):
            return []   


def save_ticket(ticket):
    JSON_FILE.parent.mkdir(parents=True, exists_ok=True)

    tickets = load_ticket()
    tickets.append(ticket)
    with open(JSON_FILE, "w") as file:
         json.dump(tickets,file, intend=4)
    print("ticket r=creat succeessfully")     