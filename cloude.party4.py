fines = {}
active = True
while active :
    name = input("what is your name?")
    if name < "done":
        break
    overdue_request = int(input("how many days overdue?"))
    fines[name] = overdue_request * 0.25

    answer = input("Add another user?(yes/no)")
    if answer == "no":
        active = False
for names, overdue_requests in fines.items():
    print(f"{names}'s borrowed {overdue_requests}$")


