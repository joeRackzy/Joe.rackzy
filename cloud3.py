return_cart = ["suger girl", 
               "story my mother told me",
                "sweet sixteen",
                "the lion and the juewl",
                "this is fate"
                ]
shelved_books = []

while return_cart :
    books = return_cart.pop()
    print(f"Shelved: {books.title()}")
    shelved_books.append(books)
    adding_book = "early ages"
shelved_books.append(adding_book)
while shelved_books.count(adding_book) == 1 :
    shelved_books.remove(adding_book)

print(f"return_cart is {len(return_cart)}\n")
print(f"shelved_books is now {len(shelved_books)}")
