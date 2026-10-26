from pathlib import Path
import json

JSON_FILE = Path(__file__).resolve().parent / "work_flow.json"
# JSON_FILE = Path(__file__).resolve().parent / "work_flow.json"


def welcome():
    print("WELCOME TO THE CAMPUSFLOW SYSTEM")
    print("================================")


def student_name():
    name = input("Enter your name: ").strip()
    print(f"Hello {name.title()}.")
    return name


def choose_option():
    print("\nTICKET MENU")
    print("1. Name")
    print("2. Check Fees")
    print("3. Issues")
    print("4. Priority")
    print("5. Save ticket")
    print("6. Load tickets")
    print("7. Logout\n")


def school_fees():
    print("Choose a number for your fee status:")
    print("1. I have not paid")
    print("2. I paid part payment")
    print("3. I have paid")

    while True:
        try:
            fees = int(input("Choose a number for your fee status: ").strip())
        except ValueError:
            print("Invalid input. Please choose 1, 2, or 3.")
            continue

        if fees in (1, 2, 3):
            if fees == 1:
                print("You have not paid.")
            elif fees == 2:
                print("You paid part payment.")
            else:
                print("You have paid.")
            return fees

        print("Invalid fee option. Please choose 1, 2, or 3.")


def issues():
    issue = input("What is your issue? ").strip()
    return issue


def priority():
    print("Choose your priority:")
    print("1. Low")
    print("2. Medium")
    print("3. High")
    print("4. Critical\n")

    while True:
        try:
            pri = int(input("Choose a number of your priority: ").strip())
        except ValueError:
            print("Invalid input. Please choose from 1 to 4.")
            continue

        if pri in (1, 2, 3, 4):
            if pri == 1:
                print("Low")
            elif pri == 2:
                print("Medium")
            elif pri == 3:
                print("High")
            else:
                print("Critical")
            return pri

        print("Invalid priority. Please choose from 1 to 4.")


def quit():
    print("Goodbye!\n")


def load_tickets():
    if not JSON_FILE.exists():
        return []

    try:
        with open(JSON_FILE, "r") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_ticket(ticket):
    tickets = load_tickets()
    tickets.append(ticket)

    with open(JSON_FILE, "w") as file:
        json.dump(tickets, file, indent=4)

    print("Ticket saved successfully.")


def main():
    welcome()
    ticket = {}

    while True:
        choose_option()

        try:
            choice = int(input("Enter your choice from 1 to 7: ").strip())
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 7.")
            continue

        if choice == 1:
            ticket["Name"] = student_name()
        elif choice == 2:
            ticket["school_fees"] = school_fees()
        elif choice == 3:
            ticket["issues"] = issues()
        elif choice == 4:
            ticket["priority"] = priority()
        elif choice == 5:
            required_fields = ["Name", "school_fees", "issues", "priority"]
            missing = [field for field in required_fields if field not in ticket]

            if missing:
                print(f"You are missing: {', '.join(missing)}")
                print("Complete options 1 to 4 before saving.")
                continue

            save_ticket(ticket)
            ticket = {}
            print("Returning to the menu...\n")
        elif choice == 6:
            tickets = load_tickets()
            if tickets:
                
                print(json.dumps(tickets, indent=4))
            else:
                print("No tickets found.")
        elif choice == 7:
            quit()
            break
        else:
            print("Invalid input. Please choose from 1 to 7.")


if __name__ == "__main__":
    main()


