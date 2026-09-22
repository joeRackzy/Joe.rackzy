snack_orders = {}
active = True
while active:
    names = input("what is yo name?")
    
    ages = input("how old are you?")
    ages = int(ages)
    if not names:
           break

    snack_orders[names] = ages
    question = input("add another?(yes/no)")
    if question == "no":
        active = False        

