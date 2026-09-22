checking_ages = True
respond ={}
while checking_ages:
    name = input("what is you name ?")
    age = input("what is your age?")
    quit = input("are you done ?")
   
   
    if age == "done":
        checking_ages = False
        continue
    age = int(age)
    if age < 0:
        print("erorr")
        continue

    elif age < 13:
        print("you can only watch PG movies;")
    else:
        print("you can watch!") 
    respond[name] = age  
    if quit == "yes":
           break
      

print("\n\t-----finish checking everything---")
for names,ages in respond.items():
    print(f"{names} is {ages} years old")

    
