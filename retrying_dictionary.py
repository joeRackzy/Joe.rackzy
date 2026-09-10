persons = {
    "first_name": "samuel",
    "last_name": "paul",
    "city": "lafia",
    "age": 34,
}
print(persons["first_name"])
print(persons["last_name"])
print(persons["city"])
print(persons["age"])


favorite_numbers = {
    "faith": 43,
    "peace": 2,
    "jane": 5,
    "Grace": 6
}
favorite_numbers["joseph"] = 3
favorite_numbers["peter"] = 8
favorite_numbers["sunday"] = 4

print(favorite_numbers)
for name, number in favorite_numbers.items(): 

    print(f"{name}'s favorite number is {number}")

 