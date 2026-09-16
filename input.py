Age = input("how olg are you?")
Age =int(Age)
if Age <= 18:
    print("you are not an adult")
elif Age >= 58:
    name = input("input your energy test result")
    name = float(name)
    if name >= 58.3:
        print("you are fit")
    else:
        print("you need to work on your enegy")   

          
    print("you are welcome to the fellow")    
else:
    print("you are an adult")    


Rental_car = input("What kind of rental car would you like?")
print("let me see if i can find a" + Rental_car)

Restaurant_seating = input("how many people are in their dinning group?")
Restaurant_seating = int(Restaurant_seating)
if Restaurant_seating > 8:
    print("they will have to wait for a Table.")
else:
    print("their table is ready.")  

Multiples_of_ten = input(" give me a number and i willl show you if the number is a" 
                                       "even number or odd number")
Multiples_of_ten = int(Multiples_of_ten)
if Multiples_of_ten % 2 == 0:
    print(f"{Multiples_of_ten}this is a even number.")
else:
    print(f"{Multiples_of_ten}this is a odd number.")     
