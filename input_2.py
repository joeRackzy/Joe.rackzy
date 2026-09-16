prompt = ""
prompt += input("\nas long as the is not 'quite'.")

massage = ""
while massage != "quite.":
    massage = input(prompt)
    if massage != "quite.":
        print(massage)

number = 0
while number < 11:
    number += 1
    print(number)

# that means the game is still on
game = True
while game:
    massa = prompt
    if massa == "quite":
        # the game should off
        game = False 
    else:
        print(massa)  
        print("we arae still on the game")
print("Game off")            