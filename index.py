menu={'maggie':100,'noodles':200,"coffee":75,"Green Tea":30,"Chocolate Truffle Supreme Delight Pastry":70}
amount=0
def ttl_bill(item):
    global amount
    if item in menu:
        print(f"The amount for {item} is",menu[item])
        amount+=menu[item]
        print("Do you want to add another item type y/n")
        if input()=="y":
            item=input("Type the item you want to order ")
            ttl_bill(item)
        else:
            print("The total bill is",amount)
            print("ThankYou Visit Again!!!")
    
print("-*"*7+"WELCOME"+"*-"*7,"\nWould you like to order something type yes/no")
z=input()
if z=="yes":
    print("Here is the menu Card")
    for i in menu:
        print(i)
    item=input("Type the item you want to order ")
    ttl_bill(item)   
else:
    print("Thank You Visit Again!!!")




        
        











