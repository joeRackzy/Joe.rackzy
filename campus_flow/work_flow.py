import json
from pathlib import Path
JSON_FILE = Path(__file__).resolve().parent / "work_flow.json"
     
def creat_menu():
    print("1. name".title())
    print("2. check fees".title())
    print("3. issue".title())
    print("4. priority")
    print("5. save ticket".title())
    print("6. load ticket".title())
    print("7. logout\n")

def student_name():
    name = input("what is your name? ".title().strip())
    return name    

def school_fees():
    print("1. i have paid")
    print("2. i only paid half of the fees")
    print("3. i have not pay\n".upper())

    while True:
        try:
            fees = int(input("Have You Paid Your School Fees?\n choose from 1,2,3"))
        except ValueError:
            return "invalid input try again, choos from 1,2,3".title()
        if fees in (1,2,3):
            if fees == 1:
                pay = "i have paid"
                print(pay)
            elif fees == 2:
                pay = "i only paid half of the fees"
                print(pay)     
            else:
                pay = "i have not pay".upper()
                print(pay)  
        return pay       

def issues():
    question = input("what are the problem you are facing ".title())
    return question

def priority():
    print("1. low")        
    print("2. medium")
    print("3. high")
    print("4. critical")

    while True:
        try:
            prio = int(input("how critical is you issuse?"))
        except ValueError:
            return "invalid input try again. choos from 1,2,3,4".title()
        if prio in (1,2,3,4):
            if prio == 1:
                level = "low".title()
                print(level)
            elif prio == 2:
                level = "medium".title()
                print(level)
            elif prio == 3:
                level = "high".title()
            else:
                level = "critical".title() 
                print(level)
        return  level     
def welcome():
    print("========================================")
    print("you are welcome to campus flow".upper())
    print("========================================\n")    
def load_ticket():
    if not JSON_FILE.exists():
        return []
    try:
        with open(JSON_FILE , "r") as file:
            return json.load(file)
    except json.JSONDecodeError:   
        return []
tickets = []
def save_ticket(ticket):

    tickets = load_ticket()
    if not isinstance(tickets, list):
        return []

    tickets.append(ticket)

    with open(JSON_FILE, "w") as file:
        json.dump(tickets,file, indent=4)


def main():
    ticket ={
     
    }
    welcome()
    while True:
        
        print("\t","choose an option".upper())
        creat_menu()     
def creat_menu():
    print("1. name".title())
    print("2. check fees".title())
    print("3. issue".title())
    print("4. priority")
    print("5. save ticket".title())
    print("6. load ticket".title())
    print("7. logout\n")

def student_name():
    name = input("what is your name? ".title().strip())
    return name    

def school_fees():
    print("1. i have paid")
    print("2. i only paid half of the fees")
    print("3. i have not pay\n".upper())

    while True:
        try:
            fees = int(input("Have You Paid Your School Fees?\n choose from 1,2,3"))
        except ValueError:
            return "invalid input try again, choos from 1,2,3".title()
        if fees in (1,2,3):
            if fees == 1:
                pay = "i have paid"
                print(pay)
            elif fees == 2:
                pay = "i only paid half of the fees"
                print(pay)     
            else:
                pay = "i have not pay".upper()
                print(pay)  
        return pay       

def issues():
    question = input("what are the problem you are facing ".title())
    return question

def priority():
    print("1. low")        
    print("2. medium")
    print("3. high")
    print("4. critical")

    while True:
        try:
            prio = int(input("how critical is you issuse?"))
        except ValueError:
            return "invalid input try again. choos from 1,2,3,4".title()
        if prio in (1,2,3,4):
            if prio == 1:
                level = "low".title()
                print(level)
            elif prio == 2:
                level = "medium".title()
                print(level)
            elif prio == 3:
                level = "high".title()
            else:
                level = "critical".title() 
                print(level)
        return  level     
def welcome():
    print("========================================")
    print("you are welcome to campus flow".upper())
    print("========================================\n")

def main():
    welcome()
    while True:
        print("\t choose an option".upper())
        creat_menu()
        try:
            choice = int(input("choose from 1,2,3,4,5,6,7- "))
        except ValueError:
            print("invalid input try again form 1,2,3,4,5,6,7")
            continue
        if choice == 1:
            ticket["Name"] = student_name()

        elif choice == 2:
             ticket["fees"] = school_fees()
        elif choice == 3:
             ticket["issue"] = issues()
        elif choice == 4:
             ticket["priority"] = priority()
        elif choice == 5:
            if "Name" not in ticket or "fees" not in ticket or "issue" not in ticket or "priority" not in ticket:
                print("ohh Snap! no ticket found try again from 1 -7")
                continue
    
            save_ticket(ticket)
            ticket = {}
            print("!Bim ticket has been save save Successfully".strip()) 


        elif choice == 6:
            tickets = load_ticket() 
            if not tickets:
                print("No saved tickets found.\n")
            else:
                print("\n--- ALL SAVED TICKETS ---")
                for index, t in enumerate(tickets, start=1):
                    print(f"T0{index}:\t")
                    print(json.dumps(t, indent=4))
                
          
        elif choice == 7:
            print("good bye")
            break
        elif choice >= 8:
            print("invalid option try again from 1,2,3,4,5,6,7")                      



if __name__ == "__main__":
    main()



     
