claude_Guests = ["Alice", "Bob", "faith","Charlie", "David", "Joseph"]
for Guest in claude_Guests:
    print(f"hi {Guest}: you are invited to a diiner in my house tonight.")
claude_Guests.remove("Alice")  
print("\nsomebody is not comming to the dinnerto nightso we remove him for the list")  
claude_Guests.insert(0,"Jene")

for Guest in claude_Guests:
    
    print((Guest))
sorted_list = sorted(claude_Guests)
print(f"the is the sorted list \n{sorted_list}")
print(f"this is the original list \n{claude_Guests}")
# while len(claude_Guests) > 0:
#     removed_Guest = claude_Guests.pop()
#     print(f"removed {removed_Guest} from the list")
Guest_count = len(claude_Guests)
print(f"the number of guests remaining is: {Guest_count}")

Guest_seat = list(range(1,7))
for number, value in enumerate(claude_Guests):
    print(f"{value} is assigned to seat on a number {Guest_seat[number]}")
