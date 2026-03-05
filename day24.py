# Mini Bank Account System 
bank={}
while True:
    try:
        user=int(input("1.Create Account\n2.Deposit Money\n3.Withdraw\n4.Chake balance\n5.Show all account\n6.Exit\nPlease Select Menu option: "))
        if user==1:
            name=input("Please enter the name: ")
            if name in bank:
                print("Already exist")
            else:
                balance=int(input("First deposit: "))
                a=bank[name]=balance
                print(f"Create account{name} first deposit{a}")
        elif user==2:
            name=input("Please enter your name: ")
            if name in bank:
                deposit=int(input("Enter money: "))
                bank[name]=bank[name]+deposit
                print(f"New balance{bank[name]}")
            else:
                print("Account not found!")
        elif user==3:
            name=input("Please ente name: ")
            if name in bank:
                withdraw=int(input("Enter money: "))
                if withdraw<bank[name]:
                    bank[name]=bank[name]-withdraw
                    print(f"Remaining balance{bank[name]}")
                else:
                    print("Insufficient balance")
            else:
                ("Account not found!")
        elif user==4:
            name=input("Enter name: ")
            if name in bank:
                print(f"{bank[name]}rupees")
            else:
                print("Account not found")
        elif user==5:
            for name in bank.keys():
                print(f"Customer {name} Rupees {bank[name]}")
        else:
            user==6
            print("Exit")
            break
    except:
        print("Worng input")                        




