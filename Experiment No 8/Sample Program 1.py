class Account:
    def __init__(self, accnumber, balance):
        self._accnumber = accnumber
        self._balance = balance

class SBAccount(Account):
    def __init__(self, acc_number, balance):
        super().__init__(acc_number, balance)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}. New balance: {self._balance}")

    def withdraw(self, amount):
        if self._balance - amount > 1000:
            self._balance -= amount
            print(f"Withdrew: {amount}. New balance: {self._balance}")
        else:
            print("Insufficient Balance !!!")

    def calc_interest(self):
        interest = 0.04 * self._balance
        self._balance += interest
        print(f"Interest credited: {interest}. New balance: {self._balance}")

class FDAccount(Account):
    def __init__(self, accno, period, deposit_amt):
        super().__init__(accno, deposit_amt)
        self.period = period

    def calc_interest(self):
        interest = (8.25 / 100) * self._balance * self.period
        return interest

    def close(self):
        interest = self.calc_interest()
        self._balance += interest
        print(f"FD closed. Interest credited: {interest}. Final balance: {self._balance}")

class Customer:
    def __init__(self, cust_id, name, address):
        self.cust_id = cust_id
        self.name = name
        self.address = address
        self.sb = None
        self.fd = None

    def createAccount(self, acc_type, accno, period, balance):
        if acc_type == "SB":
            self.sb = SBAccount(accno, balance)
            print(f"SB Account created for {self.name}.")
        elif acc_type == "FD":
            self.fd = FDAccount(accno, period, balance)
            print(f"FD Account created for {self.name}.")

    def transaction(self, acc_type, operation, amount):
        if acc_type == "SB" and self.sb:
            if operation == "withdraw":
                self.sb.withdraw(amount)
            elif operation == "deposit":
                self.sb.deposit(amount)
            elif operation == "calculate interest":
                self.sb.calc_interest()
            else:
                print("Invalid operation for SBAccount.")
        elif acc_type == "FD" and self.fd:
            if operation == "close":
                self.fd.close()
            else:
                print("Invalid operation for FDAccount.")
        else:
            print(f"No {acc_type} Account found.")

class BankDemo:
    def main():
        customers = []
        n = int(input("Enter the Number of Customers to be Added: "))
        for i in range(n):
            print("Customer No:", i + 1)
            cust_id = int(input("Enter the Customer ID: "))
            name = input("Enter the Customer Name: ")
            address = input("Enter the Customer Address: ")
            customers.append(Customer(cust_id, name, address))
            print("Customer Details Added Successfully!\n")
            print("Which Account Do you want to Create:")
            print("1. SB Account")
            print("2. FD Account")
            acc_type = input("Enter Your Choice (SB/FD): ")
            if acc_type == "SB":
                accno = int(input("Enter Account Number: "))
                balance = float(input("Enter the Balance Amount: "))
                customers[i].createAccount(acc_type, accno, 0, balance)
            elif acc_type == "FD":
                accno = int(input("Enter the Account Number: "))
                period = int(input("Enter the Period (in years): "))
                balance = float(input("Enter the Balance Amount: "))
                customers[i].createAccount(acc_type, accno, period, balance)

            print("Which Operation to be Performed:")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Calculate Interest")
            print("4. Close FD Account")
            operation = input("Enter Your Operation: ")
            amount = float(input(f"Enter the Amount for {operation}: "))
            customers[i].transaction(acc_type, operation, amount)

if __name__ == "__main__":
    BankDemo.main()
