lents= ["mango", "car", "elephant", "international", "community", "you", "go", "i"]
len(lents)
for lent in sorted(lents, key=len):

   print(f"= {lent} {len(lents)}")