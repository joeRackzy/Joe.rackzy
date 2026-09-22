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
print("\t-----result for snack orders-------")   
for name, age in snack_orders.items()  :
     print(f"{name} is {age} years old")

