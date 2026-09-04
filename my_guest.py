Guests = ["mary", "jenny", "peter"]
Guests.sort(reverse=True)
print(Guests)
Guests[1] = "mike"
for guest in Guests:
    print(f"you are invited to dinner {guest}")
for list in Guests:    
  print(f"{list} you are still invited")
  sorted_Guests = Guests.sort()    
print("opps i found a bigger table so i will have to invite more people to the dinner")  
Guests.insert(0, "faith")
Guests.insert(2, "favor")
Guests.append("john")

print(Guests)
print("")
for list in Guests:
   print(f"{list}: you are invited to the dinner")
print(" I can only invite 2 persons to the dinner")   
while len(Guests) > 2:
   removing_guest = Guests.pop()
   print(f"Dear {removing_guest} i am sorry i can't invite you to dinner.")
for list in Guests:
  print(f"{list}: you are still invited")   
del Guests[:]
print(Guests)  

    
