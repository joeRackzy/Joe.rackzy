
result = {}
active = True 

while active:
    name = input("what is you name?")
    voter_ID = input("insert your ID")
    voter_ID = int(voter_ID)
    if voter_ID == 1234:
        print(F"{name.upper()} you are  welcome to the poly unit")
    else:
        print("invalid ID")
        print("opps!!")
        continue
    candidate = input("who are you voting for today?(joseph/peter)")
    if candidate == "peter":
        print(f"{name} you have voted for peter!")
        
    elif candidate == "joseph":
        print(f"{name} you have just voted for joseph")
        
    else:
        print("invalid candidate")
        break
    adding = input("is there anyone who is votiong again(yes/no)")
    if adding == "no":
        active = False
    result[name] = candidate    
print("----election_result----") 
for names,candidates in  result.items():
    print(f"{names} voted for {candidates}") 
print("\n-----------the final result for the election-----")
       
        
 

     