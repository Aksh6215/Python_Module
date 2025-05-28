# Bank Console

Balance1 = 0.0
Balance2 = 0.0

user1 = "aksh12"
password1 = "1234"

user2 = "aman34"
password2 = "5678"

while True:
    print("\n------ WELCOME TO THE BANK! ------")
    id = input("ENTER YOUR ID : ")
    code = input("ENTER YOUR PASSWORD : ")

    if id == user1 and code == password1:
        while True:
            choice = int(input("\nWhat you want to do ? \n1. Deposit\n2. Withdraw\n3. Display Balance\n4. Send Money\n5. Sign out\nEnter your choice : "))

            if choice == 1:
                deposit = float(input("\nEnter the amount to deposit : "))
                Balance1 += deposit
                print("Balance after deposit =", Balance1)

            elif choice == 2:
                withdraw = float(input("\nEnter the amount to withdraw : "))

                if withdraw > Balance1:
                    print("Insufficient Balance!")
                else:
                    Balance1 -= withdraw
                    print("Balance after withdraw =", Balance1)

            elif choice == 3:
                print ("\nYour Balance =", Balance1)

            elif choice == 4:
                SendMoney = float(input("\nEnter amount to be transferred : "))
                if SendMoney > Balance1:
                    print("Insufficient Balance!")
                    break
                else:
                    receiver = input("\nEnter the receiver id : ")
                    if receiver == user2:
                        Balance2 += SendMoney
                        Balance1 -= SendMoney
                        print("Available balance =", Balance1)
                    else:
                        print("Try Again")
            elif choice == 5:
                break
            else:
                print("Exiting...")
                break
   
    elif id == user2 and code == password2:
        while True:
            choice = int(input("\nWhat you want to do ? \n1. Deposit\n2. Withdraw\n3. Display Balance\n4. Send Money\n5. Sign out\nEnter your choice : "))

            if choice == 1:
                deposit = float(input("\nEnter the amount to deposit : "))
                Balance2 += deposit
                print("Amount after deposit =", Balance2)

            elif choice == 2:
                withdraw = float(input("\nEnter the amount to withdraw : "))

                if withdraw > Balance2:
                    print("Insufficient Balance!")
                else:
                    Balance2 -= withdraw
                    print("Balance after withdraw =", Balance2)

            elif choice == 3:
                print ("\nYour Balance =", Balance2)

            elif choice == 4:
                MoneyTransfer = float(input("Enter amount to be transferred : "))
                if MoneyTransfer > Balance2:
                    print("Insufficient Balance!")
                    break
                else:
                    receiver = input("\nEnter the receiver id : ")
                    if receiver == user1:
                        Balance1 += SendMoney
                        Balance2 -= SendMoney
                        print("Available balance =", Balance2)
                    else:
                        print("Try Again")

            elif choice == 5:
                break
            else:
                print("Exiting...")
                break
        
    else:
        print("Invalid login")