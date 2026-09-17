pizza_topping = "\nplease enter the pizza you will like to add to the topppings"
pizza_topping += "\nEnter 'quit' when you are don"

massage = ""
while massage != "quit":
    massage = input(pizza_topping)
    if massage != "quit":
         print(f"i will add {massage} to the pizza topping")
    else:
         print("thank you for yo contribution to our pizza topping")     

Movie_Ticket = "\nWhat is your age?"
Movie_Ticket += "\nand i will show you the ticket price"
while Movie_Ticket :
     age=input(Movie_Ticket)
     age = int(age)
     if age < 3:
        print("you are free to the movie theater!")
     elif age >= 3 or age <= 12:
         print("your ticket is $10")
     else:
         print("your ticket is $15")        


infinity = 1
while  infinity < 8:
    print(infinity) 
            
