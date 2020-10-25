database = {
    'reshma121': {
        'name': 'Reshma Jadhav',
        'age': 32,
        'email': 'reshma123@gmail.com',
        'pin': '1234',
        'balance': 20000,    
    },
    'shiv456': {
        'name': 'Shiv Verma',
        'age': 40,
        'email': 'shiv456@gmail.com', 
        'pin': '4567',
        'balance': 40000,  
    },
     'neha234': {
        'name': 'Neha Sawant',
        'age': 40,
        'email': 'shiv456@gmail.com', 
        'pin': '2345',
        'balance': 35000,  
    }
}

def userpwd():
    username = input("Enter username: ")
    if username not in database.keys():
        print("Username is not found")
    elif username in database.keys():
        pin = input("Enter 4 digit pin number: ")
        if pin == database[username]['pin']:
            print(f"Login Successful\nWelcome {database[username]['name']}")
            balance = database[username]['balance']
            while True:
                acct = int(input("Enter your choice: \n1. Withdrawl\n2. Deposit Balance\n3. Check Balance\n4. Logout\n"))
                if acct == 4:
                    print("You are successfully logout")
                    break
                elif acct == 1:
                    print("Your Balance: ", balance)
                    withdraw = int(input("Enter Withdraw amount: "))
                    if withdraw > balance:
                        print("Insufficient Balance") 
                    elif withdraw > 0:
                        balance = balance - withdraw
                        print("Total Balance: ", balance)
                    else:
                        print("Withdrawl not done")
                elif acct == 2:
                    print("Your Balance: ", balance)
                    deposit = int(input("Enter deposit amount: "))
                    if deposit > 0:
                        balance = balance + deposit
                        print("Total Balance: ", balance)
                    else:
                        print("Amount not deposited") 
                elif acct == 3:  
                    print("Your Balance: ", balance)
        else:
            print("Incorrect pin number")
            forgotpwd()
    else:
        return 


def forgotpwd():
    for_pwd = input("forgot your pin number: yes/no ")
    if for_pwd == 'yes':
        username = input("Enter username: ")
        if username in database.keys():
            new_pin = input("Enter new 4 digit pin number: ")
            database[username]['pin'] = new_pin
            print(database[username])
            print("Your new pin number updated")
            return
        else:
            userpwd()  
        

def signup():  
    username = input("Enter your username: ")
    if username in database.keys():
        print("This Username already Exists")
        return
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    email = input("Enter your email: ")
    pin = int(input("Enter 4 digit pin number: "))
    balance = int(input("Enter balance in your account: "))
    newdict = dict(username=username, name=name, age=age,  email=email,  pin=pin, balance=balance)
    print(newdict)  
    print("Account successfully created")

while True: 
    choice = int(input("Enter your choice: \n1. Login\n2. Signup \n3. Exit\n"))
    if choice == 3:
        break
    elif choice == 1:
        userpwd()
    elif choice == 2:
        signup()
        