movies = {
    "Inception":{
        "Director": "Inass",
        "Year": 2025,
        "Rating": 4.6
    },
    "coco":{
        "Director": "Sunny young",
        "Year": 2018,
        "Rating": 4.9
    },
    "Gift from the Gods":{
        "Director": "Mikky",
        "Year": 2025,
        "Rating":4.8
    }
}
for title, information in movies.items():
    print(f"\nMovie. {title.upper()}.")
    informations = f"Directed by: {information["Director"]}\n\tReleased:{ information["Year"]}\n \tRating:{information["Rating"]}"

    print(f"\t{informations}")
coco = movies["coco"]["Director"]
print(f"\n{coco}")