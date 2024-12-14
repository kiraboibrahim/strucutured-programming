SEND_MONEY = "1"
BUY_AIRTIME = "2"
WITHDRAW_MONEY = "3"
EXIT = "4"

customers = {
    "0709645302": {
        "name": "Ibrahim Kirabo Ssemmambo",
        "contact": "0709645302",
        "pin": "1000",
        "account_balance": 1000000,
    },
    "0750683748": {
        "name": "Mupere Nathan",
        "contact": "0750683748",
        "pin": "2000",
        "account_balance": 2000000,
    },
    "0752589908": {
        "name": "Kasirye Shafic",
        "contact": "0752589908",
        "pin": "3000",
        "account_balance": 40000,
    },
    "0778014203": {
        "name": "Matovu Kizito",
        "contact": "0778014203",
        "pin": "4000",
        "account_balance": 2000,
    },
    "0705378073": {
        "name": "Bashabe Jackline",
        "contact": "0705378073",
        "pin": "5000",
        "account_balance": 10000,
    },    
}

def verify_pin(user_number, user_pin):
    customer = customers[user_number]
    if customer['pin'] == user_pin:
        return True
    else:
        return False


def send_money(sender_number, recipient_number, sent_amount):
    sender = customers[sender_number]
    if sender['account_balance'] >= sent_amount:
        customers[sender_number]['account_balance'] -= sent_amount
        customers[recipient_number]['account_balance'] += sent_amount

def buy_airtime(user_number, airtime_amount):
    if airtime_amount <= customers[user_number]["account_balance"]:
        customers[user_number]["account_balance"] -= airtime_amount

def withdraw_money(user_number, withdraw_amount,):
    if withdraw_amount >= 5000 and customers[user_number]['account_balance'] >= withdraw_amount:
       customers[user_number]['account_balance'] -= withdraw_amount

def print_balance(user_number):
    print(f"Your account balance is: {customers[user_number]['account_balance']}")

def print_menu():
    print("1. Send money")
    print("2. Buy airtime")
    print("3. Withdraw")
    print("4. Exit")


user_number = input("Enter your mobile number: ")

while True:
    print()
    print_menu()

    selected_option = input("Choose option: ")
    if selected_option == SEND_MONEY:
        recipient_number = input("Recipient's number: ")
        sent_amount = int(input("Amount: "))
        pin = input("Mobile Money PIN: ")
        is_valid_pin = verify_pin(user_number, pin)
        if is_valid_pin:
            send_money(user_number, recipient_number, sent_amount)
            print_balance(user_number)
        else:
            print("Invalid PIN!")
    elif selected_option == BUY_AIRTIME:
        airtime_amount = int(input("How much airtime: "))
        pin = input("Mobile money PIN: ")
        is_valid_pin = verify_pin(user_number, pin)
        if is_valid_pin:
            buy_airtime(user_number, airtime_amount)
            print_balance(user_number)
        else:
            print("Invalid PIN!")
    elif selected_option == WITHDRAW_MONEY:
        withdraw_amount = int(input("How much are you withdrawing?: "))
        pin = input("Mobile money PIN: ")
        is_valid_pin = verify_pin(user_number, pin)
        if is_valid_pin:
            withdraw_money(user_number, withdraw_amount)
            print_balance(user_number)
        else:
            print("Invalid PIN!")
    elif selected_option == EXIT:
        break
    else:
        print("Invalid option selected")