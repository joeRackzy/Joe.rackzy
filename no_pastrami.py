ask = {}
active = True
while active:
    names = input("\nwhat is your name?")
    questions = input("\nwere would you to visite someday?")
    ask[names] = questions
    respond =input("would you like let somebody to joing the  poll?(yes/no)?")
    if respond == "no":
        active = False
print("----- poll Results-----\n")
for name, que in ask.items():
    print(f"{name} said he would love to visit {que}")       
