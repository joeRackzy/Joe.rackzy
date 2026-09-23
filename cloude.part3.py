checking_out = True
while checking_out:
    title_for_books = input("which kind of book do you like?")
    if title_for_books == "done":
        checking_out = False
        continue
    copy = input("how many copies  would you like to have?")
    copy = int(copy)
    if copy <= 0 :
        print("error")
        continue
    else:
        print("checking out X copies remaining")
    print(f"check out {copy} remeaning")    

print("check out is completed ")    


