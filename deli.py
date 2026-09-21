sandwish_orders =["show", "YBNL", "content creator", "canada", "LonDon"]
finished_sandwiches = []
while sandwish_orders:
    procesing = sandwish_orders.pop()
    print(f"{procesing} is the place i would lov eto go somedays")
    finished_sandwiches.append(procesing)
print("\n------ this are my wishes-----")
for wish in finished_sandwiches:
    print(f"-{wish}")        