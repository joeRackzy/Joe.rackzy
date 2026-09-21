ask = "tell me sothing and i will repeat it to you"
ask += "\nEnter 'quit' if you want to end the program"

message = ""
active = True
while active:
    message =input(ask)
    if message == " quit":
        active = False
    elif message == "time out":
        active = False   
    elif message == "out of life":
        active = False   
    else:
        print(f"you are wellcome {message}")



while True:
    user = input("what is your name?")
    mesaage =input("which city would you like to visit")
    if mesaage == "quit":
        break
    else:
        print(f"{user.title()} said he would like to visit {mesaage.title()}.")
    print(f"{user} like to visit {mesaage}")


i = 1
while i <= 3:
    i += 1
  
    print(i)
for i in range(2):
    for j in range(3):
        print(f"{i}{j}")