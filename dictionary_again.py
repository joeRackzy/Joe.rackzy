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
        "favor": "Ruby",
        "peace": "C++"
}    
for names in people:
    if names in favorite_language:
        print(f"{names} thank you for taking the poll")
    else:
        print(f"{names} please make sure you take the poll as soon as posible")    