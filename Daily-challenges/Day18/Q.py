'''Build a BankAccount class with an instance variable balance
 initialized to 0. Write three methods: deposit(amount), 
 withdraw(amount) (prevent overdrafts), and display_balance()'''

class BankAccount:
    def __init__(self):
        # Initialize instance variable balance to 0
        self.balance = 0

    def deposit(self, amount):
        """Adds the specified amount to the balance."""
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Subtracts amount from balance if sufficient funds exist to prevent overdrafts."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Successfully withdrew ${amount:.2f}")
            else:
                print("Transaction declined: Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        """Prints the current account balance."""
        print(f"Current Balance: ${self.balance:.2f}")


# --- Execution Example ---
if __name__ == "__main__":
    # Create an account instance
    account = BankAccount()
    
    # 1. Check initial balance
    account.display_balance()  # Expected: $0.00
    
    # 2. Deposit money
    account.deposit(150.50)
    account.display_balance()  # Expected: $150.50
    
    # 3. Attempt overdraft withdrawal
    account.withdraw(200.00)   # Expected: Decline message
    
    # 4. Successful withdrawal
    account.withdraw(50.00)
    account.display_balance()  # Expected: $100.50

