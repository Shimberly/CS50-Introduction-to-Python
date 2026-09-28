# Global variable
balance = 0

def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)

def deposit(n):
    # this will give error: UnboundLocalError: cannot access local variable 'balance' where it is not associated with a value
    # you can read global variables but not change them
    # balance += n

    global balance
    balance += n
    
def withdraw(n):
    global balance
    balance -= n    

if __name__ == "__main__":
    main()