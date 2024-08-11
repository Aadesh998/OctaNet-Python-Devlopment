class ATM:
    def __init__(self, pin, initial_balance=0):
        """
        Initialize an ATM object with a PIN, an initial balance, and an empty transaction history.
        """
        self.balance = initial_balance
        self.pin = pin
        self.transaction_history = []

    def check_balance(self):
        """
        Return the current balance of the account.
        """
        return self.balance

    def cash_withdrawal(self, amount):
        """
        Withdraw the specified amount from the account if sufficient balance is available.
        Update the balance and record the transaction in the transaction history.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            print(f"${amount} withdrew successfully")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            print("Invalid withdrawal amount.")

    def cash_deposit(self, amount):
        """
        Deposit the specified amount into the account if the amount is valid.
        Update the balance and record the transaction in the transaction history.
        """
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            print(f"${amount} deposited successfully")
        else:
            print("Invalid amount.")

    def pin_change(self, old_pin):
        """
        Change the PIN of the account if the old PIN is correct.
        """
        if self.pin == old_pin:
            new_pin = int(input("Enter a new PIN: "))
            self.pin = new_pin
            print("PIN has been successfully changed.")
        else:
            print("Incorrect old PIN.")

    def print_transaction_history(self):
        """
        Print the transaction history if available, otherwise inform the user that there's no history.
        """
        if not self.transaction_history:
            print("No transaction history.")
        else:
            for transaction in self.transaction_history:
                print(transaction)

def main_menu():
    """
    Main menu for interacting with the ATM system.
    Allows the user to select various options like checking balance, withdrawing/depositing cash,
    changing PIN, viewing transaction history, or exiting.
    """
    # Predefined users with their respective PINs and initial balances
    users = {
        "Aadesh": ATM(pin=1234, initial_balance=10000),
        "User2": ATM(pin=5678, initial_balance=5000)
    }

    while True:
        print("\nWelcome to the ATM")
        username = input("Enter your username: ")

        # Check if the username exists in the system
        if username not in users:
            print("Username not found. Try again.")
            continue

        pin = int(input("Enter your PIN: "))
        user_atm = users[username]

        # Verify the entered PIN
        if user_atm.pin != pin:
            print("Incorrect PIN. Try again.")
            continue

        while True:
            # Display menu options
            print("\n1. Account balance Inquiry")
            print("2. Cash withdrawal")
            print("3. Cash deposit")
            print("4. PIN change")
            print("5. Transaction history")
            print("6. Exit")

            choice = int(input("Choose an option: "))

            # Perform action based on user's choice
            if choice == 1:
                print(f"Current balance: ${user_atm.check_balance()}")
            elif choice == 2:
                amount = int(input("Enter the withdrawal amount: "))
                user_atm.cash_withdrawal(amount)
            elif choice == 3:
                amount = int(input("Enter the deposit amount: "))
                user_atm.cash_deposit(amount)
            elif choice == 4:
                old_pin = int(input("Enter your current PIN: "))
                user_atm.pin_change(old_pin)
            elif choice == 5:
                user_atm.print_transaction_history()
            elif choice == 6:
                print("Thank you for using the ATM.")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    # Start the ATM system
    main_menu()
