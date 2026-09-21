polling = True
reciver = {}
while polling:
     
    question = input("\nwhat is you name?")
    asking = input("which mountain would you like to visit somedays?")
    reciver[question]= asking
    proposer = input("would like to let another person respond?(yes/no)")
    if proposer == "no":
        polling = False

print("\n\t------poll Result-------") 
for name, value in reciver.items():
    print(f"{name}'s said he will like to visit {value} somedays")       