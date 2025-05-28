'''
Grocery Store Billing System

Objective:
Design a Grocery Store Billing System where users can:
-> Add items to the cart
-> Remove items from cart
-> View total bill
-> Apply discount coupons

Requirements:
-> Use a dictionary to store item prices.
-> Use a list to maintain items in the cart.
-> Implement functions for adding/removing items and calculating bills.
-> Use lambda functions for discount calculations.
'''
# Grocery Store Billing System 

Grocery = {
    "1" : ["Potato", 10],
    "2" : ["Tomato", 15],
    "3" : ["Onion", 20],
    "4" : ["Apple", 50],
    "5" : ["Banana", 25]
}

cart = []
coupons = {
    "5PER" : 0.05,
    "10PER" : 0.10,
    "15PER" : 0.15,
    "20PER" : 0.20
}

def ViewCoupons():
    for i,j in coupons.items():
        print(i, j)

def GroceryDetails():
    for i,j in Grocery.items():
        print(i, j[0], j[1])
        
def AddItems():
    item = input("Enter item id: ").strip()
    cart.append(Grocery[item])
    print("Item added to cart")
    print(cart)

def RemoveItems():
    item = input("Enter item id: ").strip()
    cart.remove(Grocery[item])
    print("Item removed from cart")
    print(cart)

def ViewCart():
    print("Items in cart: ")
    for i in cart:
        print(i, end=" ")

def TotalBill():
    total = 0
    for i in cart:
        total += i[1]
    print("\nTotal bill: ", total)
    
def Discount():
    coupon = input("\nEnter coupon code: ").strip()
    discount = coupons[coupon]
    print("\nDiscount applied: ", discount)
    total = sum(item[1] for item in cart)
    apply_discount = lambda total, discount: total - (total * discount)
    total_after_discount = apply_discount(total, discount)
    print("\nTotal bill after discount: ", total_after_discount)


print("\n----- WELCOME TO GROCERY STORE -----")
while True:
    request = int(input("\n 1. View item \n 2. Add item \n 3. Remove item \n 4. View total bill \n 5. Apply discount coupon \n 6. Exit \n Enter your choice : "))

    if request == 1:
        GroceryDetails()

    elif request == 2:
        AddItems()
        
    elif request == 3:
        RemoveItems()

    elif request == 4:
        ViewCart()
        TotalBill()

    elif request == 5:
        ViewCoupons()
        Discount()        

    elif request == 6:
        print("Exiting...")
        print("Thank you for visiting store!")
        break

    else:
        print("Invalid Input! Try Again.")
