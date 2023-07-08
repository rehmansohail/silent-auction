import art

dict={}
print(art.logo)
print("Welcome to the silent auction")
print("incase of a tie, the product will go to the first bidder")
flag=""
while 1:
    if flag=="no":
        break
    flag="a"
    name=input("What is your name?\n").lower()
    amount=int(input("What is your bid?\n"))
    if name in dict:
        print("You've already placed your bid")
    else:
        dict[name]=amount
    while 1:
        if flag=="yes" or flag=="no":
            break
        flag=input("Types 'yes' to add another bidder or type 'no' to stop\n").lower()
person=""
ans=-1
for key in dict:
    if dict[key]>ans:
        ans=dict[key]
        person=key
print(f"The item goes to {person} with bid ${ans}")