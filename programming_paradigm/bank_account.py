class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance
    
    def deposit(self, amount):
        try:
            self.account_balance += amount
        except TypeError:
            raise TypeError("The amount must be a number.")
        except Exception as e:
            raise Exception(f"An Error has occurred. {e}")
    
    def withdraw(self, amount):
        amount = float(amount)
        try:
            if amount > self.account_balance:
                return False
            self.account_balance -= amount
            return True
        except TypeError:
            raise TypeError("The amount must be a number.")
        except Exception as e:
            raise Exception(f"An Error has occurred. {e}")
    
    def display_balance(self):
        print("Current Balance: ", self.account_balance)

      