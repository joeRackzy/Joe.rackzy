food = {
    "the quality": "soft",
    "things on top": ["pepperino", "flavor"]
}
food["the quality"] = ["hard","soft", "medium"]
for quality in food["the quality"]:
    if quality == "medium":
        print(f"he orderd a pizza that the qulity is so {quality.upper()} together with")
for list in food["things on top"]:
    if list == "flavor":
        print(f"{list.upper()}")

