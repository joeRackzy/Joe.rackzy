aphabetical_older = ["egg","dog","zip", "cat", "apple", "ball"]
aphabetical_older.sort()
for list in aphabetical_older:
    print(list)

non_aphabetical = aphabetical_older.pop(-1)
print(f"{non_aphabetical.upper()}: this is not a in older")
for older in aphabetical_older:
  print(f"{older}: is a in older")    
