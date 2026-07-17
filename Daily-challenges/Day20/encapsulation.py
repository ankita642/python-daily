'''Design a BankAccount class where the account holder's __balance
is kept strictly private. Provide a public deposit(amount) method
and a withdraw(amount) method (ensure withdrawal fails if funds 
are insufficient).'''


class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        # Private attribute prefixed with double underscore
        self.__balance = max(0.0, initial_balance)

    def deposit(self, amount: float) -> None:
        """Add a positive amount to the account balance."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount:.2f}. New Balance: ${self.__balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: float) -> bool:
        """Deduct amount if funds are sufficient. Returns True if successful."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        
        if amount > self.__balance:
            print(f"Withdrawal failed: Insufficient funds. Available: ${self.__balance:.2f}")
            return False
            
        self.__balance -= amount
        print(f"Withdrew: ${amount:.2f}. Remaining Balance: ${self.__balance:.2f}")
        return True

    def get_balance(self) -> float:
        """Public getter to safely view the private balance."""
        return self.__balance


# --- Example Usage ---
if __name__ == "__main__":
    # Create account
    account = BankAccount("Alice", 100.0)

    # Test deposit
    account.deposit(50.0)

    # Test successful withdrawal
    account.withdraw(30.0)

    # Test failed withdrawal (insufficient funds)
    account.withdraw(200.0)

    # Attempting to access __balance directly will raise an AttributeError
    try:
        print(account.__balance)
    except AttributeError:
        print("Access Denied: Cannot read '__balance' directly from outside the class.")
