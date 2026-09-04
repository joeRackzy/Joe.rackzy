alphabetical_order = ["egg","dog","zip", "cat", "apple", "ball"]
alphabetical_order.insert(4,"fish")
alphabetical_order.insert(5,"key")
print("\nhere are the sorted list".upper())
print(sorted(alphabetical_order))
print("\n this are the orignal list.".upper())
print(alphabetical_order)
alphabetical_order.sort()
non_alphabetical = alphabetical_order.pop(-1)


    
print(f"{non_alphabetical}:  is not in order")
for list in alphabetical_order:
  print(f"{list}: is in order")
print("\nthis are half of  my list".upper())   
while len(alphabetical_order) >= 4:
  unsorted_alphabet = alphabetical_order.pop()
  print(f"{unsorted_alphabet}.")
print(f"this are the remaing list ".upper())  
for list in alphabetical_order:  
  print(f"{list}.")  
       
