from pathlib import Path
import json


JSON_FILE = Path(__file__).resolve().parent / "work_flow.json"

def load_ticket():
    if not JSON_FILE.exists():
        return []
    try:
        with open(JSON_FILE , "r") as file:
            return json.load(file)
    except json.JSONDecodeError:   
        return []

def save_ticket(ticket):

    tickets = load_ticket()
    if not isinstance(tickets, list):
        return []

    tickets.append(ticket)

    with open(JSON_FILE, "w") as file:
        json.dump(tickets,file, indent=4)