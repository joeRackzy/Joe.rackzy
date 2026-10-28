import json
from pathlib import Path

JSON_FILE = Path(__file__).resolve().parent / "work_flow.json"


def creat_menu():
    print("1. Name")
    print("2. Check fees")
    print("3. Issue")
    print("4. Priority")
    print("5. Save ticket")
    print("6. Load ticket")
    print("7. Logout\n")


def student_name():
    return input("What is your name? ").strip()


def school_fees():
    print("1. I have paid")
    print("2. I only paid half of the fees")
    print("3. I have not paid")

    while True:
        try:
            fees = int(input("Have you paid your school fees? Choose from 1, 2, 3: "))
        except ValueError:
            print("Invalid input. Choose from 1, 2, 3.")
            continue

        if fees == 1:
            return "I have paid"
        if fees == 2:
            return "I only paid half of the fees"
        if fees == 3:
            return "I have not paid"

        print("Invalid input. Choose from 1, 2, 3.")


def issues():
    return input("What problem are you facing? ")


def priority():
    print("1. Low")
    print("2. Medium")
    print("3. High")
    print("4. Critical")

    while True:
        try:
            prio = int(input("How critical is your issue? Choose from 1, 2, 3, 4: "))
        except ValueError:
            print("Invalid input. Choose from 1, 2, 3, 4.")
            continue

        if prio == 1:
            return "Low"
        if prio == 2:
            return "Medium"
        if prio == 3:
            return "High"
        if prio == 4:
            return "Critical"

        print("Invalid input. Choose from 1, 2, 3, 4.")


def welcome():
    print("========================================")
    print("YOU ARE WELCOME TO CAMPUS FLOW")
    print("========================================\n")


def load_ticket():
    if not JSON_FILE.exists():
        return []

    try:
        with open(JSON_FILE, "r") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_ticket(ticket):
    tickets = load_ticket()
    if not isinstance(tickets, list):
        tickets = []

    tickets.append(ticket)

    with open(JSON_FILE, "w") as file:
        json.dump(tickets, file, indent=4)


def main():
    welcome()
    ticket = {}

    while True:
        print("\tCHOOSE AN OPTION")
        creat_menu()

        try:
            choice = int(input("Choose from 1, 2, 3, 4, 5, 6, 7: "))
        except ValueError:
            print("Invalid input. Try again from 1, 2, 3, 4, 5, 6, 7.")
            continue

        if choice == 1:
            ticket["Name"] = student_name()

        elif choice == 2:
            ticket["Fees"] = school_fees()

        elif choice == 3:
            ticket["Issue"] = issues()

        elif choice == 4:
            ticket["Priority"] = priority()

        elif choice == 5:
            if not all(key in ticket for key in ("Name", "Fees", "Issue", "Priority")):
                print("Oops! Ticket is incomplete. Please fill in Name, Fees, Issue, and Priority.")
                continue

            save_ticket(ticket)
            print("Ticket saved successfully.")
            ticket = {}

        elif choice == 6:
            saved_tickets = load_ticket()
            if not saved_tickets:
                print("No saved tickets found.\n")
            else:
                print("\n--- ALL SAVED TICKETS ---")
                for index, item in enumerate(saved_tickets, start=1):
                    print(f"Ticket {index}:")
                    print(json.dumps(item, indent=4))

        elif choice == 7:
            print("Goodbye")
            break

        else:
            print("Invalid option. Try again from 1, 2, 3, 4, 5, 6, 7.")


if __name__ == "__main__":
    main()
