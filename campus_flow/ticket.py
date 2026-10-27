     
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