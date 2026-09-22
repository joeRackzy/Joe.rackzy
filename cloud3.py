return_cart = ["suger girl", "chike and the river", "story my mother told me",
              "sweet sixteen", "lion and the juewl"]
shelved_books = []
while return_cart:
    book = return_cart.pop()
    print(f"{book} shelving: [title]")
    shelved_books.append(book)
print(f"{return_cart}\n")
print(f"return_cart has {len(return_cart)}") 
print(f"shalved_books has {len(shelved_books)}")  
for li in shelved_books:
    print(li) 