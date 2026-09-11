favorite_language = {
    "joseph": "python",
    "faith": "C",
    "Divine": "Golang",
    "jane": "jave script"
}
lomba = list(range(1,7))
favorite_language["mary"] = "HTML"
favorite_language["peter"] = "CSS"
for name, language in favorite_language.items():
    print(f"{name.upper()}'s favorite language is {language.upper()}.")
print("")
name_of_river = {
    "Egypt": "river Nile",
    "Nigeria": "River niger",
    "Johdan": "River Johdan"
} 
for country, River in name_of_river.items():
    print(f"{River} runs in {country}")   
print("")

people = {
      "joseph": "python",
        "faith": "C",
        "Divine": "Golang",
        "jane": "jave script",
        "fnavor": "Ruby",
        "peace": "C++"
}    
for names in people:
    if names in favorite_language:
        print(f"{names} thank you for taking the poll")
    else:
        print(f"{names} please make sure you take the poll as soon as posible")
            
# for alien_unmber in range(30):
#     listen = ["monkey", "dog", "cat", "tiger", "lion"]
#     for liste in listen:
#         print(f"{alien_unmber}: {liste}")
# print(f"{str(len(listen))}.")        

aliens = []
for alien_number in range(15):
    another = {"color": "black", "speed": "fast", "point": 10}
    aliens.append(another)

    
for al in aliens[:4]:
    if al ["point"] == 10:
        al["color"] = "white"
        al["speed"] = "slow"
        al["piont"] = 15
for alien in aliens[1:7]:
    print(alien)
print(".....")
print(f"the total number of allien is {len(aliens)}") 
  

