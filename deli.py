sandwish_orders =["show", "YBNL", "pastrami","content creator", "pastrami", "canada", "LonDon", "pastrami"]
finished_sandwiches = []
print("\n\tdeli has run out of pastrami")
while "pastrami" in sandwish_orders:
    sandwish_orders.remove("pastrami")
while sandwish_orders:
    procesing = sandwish_orders.pop()
    print(f"{procesing} is the place i would lov eto go somedays")
    finished_sandwiches.append(procesing)
print("\n------ this are my wishes-----")
for wish in finished_sandwiches:
    print(f"-{wish}")        