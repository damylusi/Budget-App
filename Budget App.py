#Budget App

class Budget():


    def __init__(self, category, balance):
        self.category = category
        self.balance = balance

    def deposit(self):
        deposit_amount = int(input('Enter amount to deposit: \n'))
        self.balance += deposit_amount
        print(f'#{self.balance}')
        return exit()

    
    def withdraw(self):
        withdraw_amount = int(input('Enter amount to withdraw: \n'))
        self.balance -= withdraw_amount
        print(f'Successful! Your new balance is #{self.balance}')
        return exit()

    def transfer(self, transfer_amt):
        print('f Transfer from {self.category} budget')
        transfer_amount = int(input('Enter amount to transfer: \n'))
        if transfer_amount >= self.balance:
            print('Insufficient funds!')
            exit()
        else:
            self.balance -= transfer_amount
            print(f'Transfer was successful. Your new {self.category} balance is #{self.balance}')
            exit()

    def balance(self):
        print(f"{self.category} balance: #{self.balance}")
        exit()


def food():
    print('Food Budget')
    food5 = Budget('food', 5000)
    food_option = input('''Select an option
        1. Deposit
        2. Withdraw
        3. Transfer
        4. Check balance \n ''')
    if food_option == '1':
        food5.deposit()
    elif food_option == '2':
        food5.withdraw()
    elif food_option == '3':
        transfer = input('''transfer to what category?
            1. clothing
            2. entertainment \n''')
        if transfer == '1':
            food5.transfer('clothing')
        elif transfer == '2':
            food5.transfer('entertainment')
        else:
            print('Invalid Option')
    elif food_option == '4':
        food5.balance()
        
    else:
        print('Invalid Option Selected')
        Welcome()

def clothing():
    print('Clothing Budget')
    clothing1 = Budget('clothing', 4000)
    clothing_option = input('''Select an option
        1. Deposit
        2. Withdraw
        3. Transfer
        4. Check balance \n ''')
    if clothing_option == '1':
        clothing1.deposit()
    elif clothing_option == '2':
        clothing1.withdraw()
    elif clothing_option == '3':
        transfer = input('''transfer to what category?
            1. food
            2. entertainment \n''')
        if transfer == '1':
            clothing1.transfer('food')
        elif transfer == '2':
            clothing1.transfer('entertainment')
        else:
            print('Invalid Option')
    elif clothing_option == '4':
        clothing1.balance()
    else:
        print('Invalid Option Selected')
        Welcome()
    
def entertainment():
    print('Entertainment Budget')
    entertainment5 = Budget('entertainment', 3000)
    entertainment_option = input('''Select an option
        1. Deposit
        2. Withdraw
        3. Transfer
        4. Check balance \n ''')
    if entertainment_option == '1':
        entertainment5.deposit()
    elif entertainment_option == '2':
        entertainment5.withdraw()
    elif entertainment_option == '3':
        transfer = input('''transfer to what category?
            1. food
            2. clothing \n''')
        if transfer == '1':
            entertainment5.transfer('food')
        elif transfer == '2':
            entertainment5.transfer('clothing')
        else:
            print('Invalid Option')
    elif entertainment_option == '4':
        entertainment5.balance()
    else:
        print('Invalid Option Selected')
        Welcome()

def Welcome():
    print('Welcome to Sunflower\'s budget')
    select_option = int(input('''What would you like to budget for?
    1. food
    2. clothing
    3. entertainment '''))
    if select_option == 1:
        food()
    elif select_option == 2:
        clothing()
    elif select_option == 3:
        entertainment()
    else:
        print('Invalid Option, Try again')
        exit()

def exit():
    exit_now = int(input("""Do you want to perform another transaction? \n
    1. Yes
    2. No \n"""))
    if exit_now == 1:
        Welcome()
    elif exit_now == 2:
        print('Thank you for recording your budget!')
    else:
        print('Invalid, Please try again')
        Welcome()

Welcome()