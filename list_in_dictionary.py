favorite_lamguage = {
    "joj": ["Python", "C", "C++", "golang"],
    "marrri": ["Ruby", "JavaScript"],
    "phillip": ["C#", "Java", "PHP"]
    }
favorite_lamguage["Grace"] = ["HTML", "CSS", "JavaScript"] 
for name,languages in favorite_lamguage.items():
    print(f"{name}'s favorite langeusge is ")
    for language in languages:
        print(f"\t{language}") 
          