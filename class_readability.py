class readability:
    def best_option(self):
        return "A"
    def test_readability():
        return reader.best_option()
    def solution():
        return reader.best_option()
    
best_option = "A"    
reader = readability()
print(f"{reader.best_option()}")  

piscription = {
    "paracitamol": "morning, aftoon,evening",
    "ampesline": "morning and evening",
    "will i be ok when i did not finish the grugs?true & false": False, 
    "how many are there in the pack": 5
}
print(piscription["paracitamol"])
print(piscription["ampesline"])
print(piscription["will i be ok when i did not finish the grugs?true & false"])
print(piscription["how many are there in the pack"])
print(" ")

names = ["joseph", "mary", "lucas", "faith", "Grace"]
print(f"i stay with {names[1]} in the same class")
print(f"i stay with {names[0]} in the same class")
print(f"i stay with {names[2].upper()} in the same class")
print(f"i stay with {names[3]} in the same class")
print(f"i stay with {names[4]} in the same class" "\n")  

for item in names:
    print("i stay with " + item.upper() + " in the same class")

guest_list = ["lucy", "Grace", "phillip"]
guest_list.sort()
print("\nso sad to hear this, that one of our guest is not going to make it to the dinner to night".upper())
del guest_list[2]
print("\nam so happy that we found a bigger dinner table for the dinner so i will need to add some people to my guest list ".upper())
guest_list.append("peter")
guest_list.append("jenny")
print(guest_list[-1])
print(guest_list[2])
print("\nDid you know that my mom call me that she willl coming with some extra tables for the dinner. So i will have to add my more guest to the list".upper())
more_guest = guest_list
more_guest.insert(0,"Emmanuel")
more_guest.insert(-1,"Sunday")
more_guest.insert(4,"Esther")

for list in more_guest:
 print(f"Dear {list} you rae cordially invited to dinner")
print("\nsorry i can in only invite 2 person to the dinner".upper())

while len(more_guest) > 2:
    remove_guest = more_guest.pop()
    print(f"i am so sorry i can't  invite {remove_guest} to the dinner to night.") 
print("my list are remaing 2 persons" "\n".upper())

for remaing in more_guest:
    print(f"{remaing.upper()}. you are still invited to the dinner")

del more_guest[-1]
del more_guest[0]     
print(f"{more_guest}")
