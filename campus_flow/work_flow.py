from ticket import school_fees,student_name,issues,creat_menu,welcome,priority
from save_and_load_ticket import load_ticket,save_ticket
tickets = []

def main():
    ticket ={
        "Name":"",
        "school_fees":"",
        "issues": "",
        "priority": ""
    }
    welcome()
    while True:
        
        print("\t","choose an option".upper())
        creat_menu()
        try:
            choice = int(input("choose from 1,2,3,4,5,6,7- "))
        except ValueError:
            print("invalid input try again form 1,2,3,4,5,6,7")
            continue
        if choice == 1:
            stu = student_name()

        elif choice == 2:
             fees = school_fees()
        elif choice == 3:
             issue = issues()
        elif choice == 4:
            priority()
        elif choice == 5:
            if ticket != {
                "Name":student_name(),
                "school_fees": school_fees(),
                "issues": issues(),
                "priority": priority()
                  }:
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
                    print(f"T{index}: {t}")
                print("--------------------------\n")
        elif choice == 7:
            print("good bye")
            break
        elif choice >= 8:
            print("invalid option try again from 1,2,3,4,5,6,7")                      



if __name__ == "__main__":
    main()





     
