Bank_Balane=10000
OLDE_PIN=1234
count=0
while (count<3):

    while(count<3):

        PIN = int(input("Enter the PIN:-"))

        if (PIN == OLDE_PIN):
            print("Enter 1 for withdraw")
            print("Enter 2 for Deposite")
            print("Enter 3 for Reset PIN ")
            print("Enter 4 for Balance enquiry")
            Open = int(input("What to open "))
            if (Open == 1):
                print("You can only withdraw the money in between 100 to 4000 ")
                print("How much do u want to Withdraw:- ")
                Withdraw = int(input())
                if (100 < Withdraw and Withdraw < 4001):
                    print("TAKE your amount", Withdraw)
                    Bank_Balane = Bank_Balane - Withdraw
                elif (100 >= Withdraw):
                    print("Small amount cant be withdraw")
                else:
                    print("That much money can not be withdraw")

            elif (Open == 2):
                print("YOU CAN ONLY Deposite MORE THAN 100")
                print("How munch do u want to Deposite")
                Deposite = int(input())
                if (100 < Deposite):
                    print("insers RS:", Deposite, "in the box")
                    Bank_Balane = Bank_Balane + Deposite
                else:
                    print("That much small amount of money can not be Deposite ")


            elif (Open == 3):
                print("Please enter the PIN")
                User_PIN = int(input())
                if (User_PIN == OLDE_PIN):
                    print("Enter the new PIN")
                    User_PIN_1 = int(input())
                    print("Enter the new PIN again")
                    User_PIN_2 = int(input())
                    if (User_PIN_1 == User_PIN_2):
                        print("Your new pass word is", User_PIN_1)
                        NEW_USER_PIN = User_PIN_1
                    else:
                        print("PINs are Not matching")
                else:
                    print("Wrong PIN")


            elif (Open == 4):
                print("Your balance is", Bank_Balane)

            else:
                print("no opt found F***")

                
        elif(PIN!=1234):
            count=count+1
            if(count==1):
                print("u have last 2 chances")
                continue
            elif(count==2):
                print("u have last 1chances")
                continue
            elif(count==3):
                print("Account blocked")
                break

print("Good bye")
