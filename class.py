reply = {}

active = True
while active:
    name = input("What is your name?")
    respond = input("Which mountain would you like to climb somedays?")
    
    question =input("would you like to let another person to reposund('yes/no')")
    reply[name] = respond
    if question == "no":
        active = False
print("----poll result----")
for name, respond in reply.items():
    print(f"{name} would to climb {respond}")

unconfirmed_user = ["joseph", "mary","peter", "faith", "peace" ]
confirmed_user = []
while unconfirmed_user:
    current_user = unconfirmed_user.pop()
    print(f"verifying user ...{current_user.title()}")
    confirmed_user.append(current_user)
print(f"\nthe following are the confirmed user...")
for name in confirmed_user:
    print(name)    