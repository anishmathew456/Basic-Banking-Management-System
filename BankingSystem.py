class Bank:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited Rs.{amount}.  Current balance Rs. {self.balance}')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"With draw Rs.{amount}. Current balance Rs.{self.balance}")
        else:
            print("insufficient balance!")

    def display_balance(self):
        print(f' Account number : {self.account_number}')
        print(f'Account holder: {self.name}')
        print(f'Balance: {self.balance}')


# Main program

account_details = {}

while True:
    print("\n" + "=" * 40)
    print("Banking Management System".center(40))
    print("=" * 40)

    print(" 1. Create Account".center(48))
    print("2. Login".center(40))
    print("3. Exit".center(40))
    choice = int(input("Enter the choice:"))
    if choice == 1:
        account_number = input("Enter the account number: ")
        name = input("Enter the account holder name: ")
        account_details[account_number] = Bank(account_number, name)

        print(f"Account created successfully for  {name}  with  A/C:{account_number}")
    elif choice == 2:
        account_number = input("Enter the account number: ")
        if account_number in account_details:
            account = account_details[account_number]
            print(f"Welcome,{account.name}!!")
            while True:
                print("\n" + "=" * 40)
                print("Account Menu".center(40))
                print("=" * 40)
                print("1. Deposit".center(40))
                print("2. Withdraw".center(41))
                print("3. Display Balance".center(47))
                print("4. Logout".center(40))
                option = int(input("Enter the option: "))
                if option == 1:
                    amount = float(input("Enter the amount to be deposited: "))
                    account.deposit(amount)
                elif option == 2:
                    amount = float(input("Enter the amount to be withdraw: "))
                    account.withdraw(amount)
                elif option == 3:
                    account.display_balance()

                elif option == 4:
                    print("Logged out")
                    break
                else:
                    print("Invalid option")
        else:
            print("Account not found !!")
    elif choice == 3:
        print("Exiting....")
        break
    else:
        print("Invalid choice !!!")
