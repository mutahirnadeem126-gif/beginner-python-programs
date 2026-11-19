class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner            # Public attribute
        self.__balance = initial_balance  # Private attribute (Encapsulation)

    # Method: Paise jama karwane ke liye
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Rs. {amount} deposited successfully!")
        else:
            print("Deposit amount positive hona chahiye!")

    # Method: Paise nikalwane ke liye
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance! Aapke paas itne paise nahi hain.")
        elif amount <= 0:
            print("Amount zero se ziada honi chahiye!")
        else:
            self.__balance -= amount
            print(f"Rs. {amount} withdrawn successfully!")

    # Method: Current Balance check karne ke liye
    def check_balance(self):
        print(f"Account Owner: {self.owner} | Current Balance: Rs. {self.__balance}")


# --- (Creating Objects) ---

# 1. account object 
account1 = BankAccount("Mutahir", 1000)

# 2. Details aur balance check 
account1.check_balance()

# 3. Deposit aur Withdraw 
account1.deposit(500)
account1.withdraw(300)

# 4. Final balance check 
account1.check_balance()

# 5. Overdraw try  (itne paise nahi hain)
account1.withdraw(2000)