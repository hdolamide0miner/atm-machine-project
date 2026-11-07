from itertools import count

current_balance = 100
n_transaction = []


def pins():
    while True:
        try:
            pin = int(input("write your pin:"))
            return pin
        except ValueError:                      # FIX: letters no longer crash it
            print("the pin must be numbers only")


def verify(pin):
    count = 0
    cpin = 2456
    while count < 3:                            # FIX: all 3 pins are now checked
        if cpin == pin:
            return True
        count += 1
        if count < 3:                           # FIX: only ask again if an attempt is left
            print("wrong pin, try again")
            pin = pins()
    print("account blocked")
    return False


def show_menu():
    print("1 == withdraw money")
    print("2 == deposit money")
    print("3 == view transactions")
    # option = int(input("put in your option:"))
    # return option


def option_input():
    while True:
        try:
            py = int(input("put in your option:"))
            return py
        except ValueError:                      # FIX: letters no longer crash it
            print("the option must be a number")


def get_amount(prompt):
    # FIX: new small helper - stops letters crashing it and stops negative/zero amounts
    while True:
        try:
            amount = int(input(prompt))
        except ValueError:
            print("please enter a whole number")
            continue
        if amount <= 0:
            print("the amount must be more than 0")
        else:
            return amount


def withdraw_money(current, with_trans):
    global current_balance
    withdraw = get_amount("how much do you want to widraw:")
    if current >= withdraw:
        current = current - withdraw
        current_balance = current_balance - withdraw
        print(current_balance)
        with_trans = (f"you withdrew ${withdraw}")
        print(with_trans)
        global n_transaction
        n_transaction.append(with_trans)
        return n_transaction
    else:
        print("you dont have enough money, you only have", current)


def deposit_money(current, dep_trans):
    global current_balance
    money = get_amount("how much do you want to deposit:")
    current = money + current
    current_balance = current_balance + money
    dep_trans = (f"you deposited ${money}")
    print(dep_trans)
    global n_transaction
    n_transaction.append(dep_trans)
    print(current_balance)
    return n_transaction


def view_transactions():
    print(n_transaction)


def query(menu):
    global current_balance
    transaction = []
    if menu == 1:
        withdraw_money(current_balance, n_transaction)
    if menu == 2:
        deposit_money(current_balance, n_transaction)
    if menu == 3:
        view_transactions()
    if menu not in [1, 2, 3]:                   # FIX: tells the user instead of doing nothing
        print("that option doesn't exist, choose 1, 2 or 3")


def main():
    verification_result = verify(pins())
    print(verification_result)
    if verification_result:
        show_menu()
        user_input = option_input()
        query(user_input)
        ask = input("do you want to perform another function :")
        while ask == "yes":
            new_main()
            ask = input("do you want to perform another function :")
    else:                                       # FIX: now lines up with "if", not "while"
        print("CARD BLOCKED! ! ")


def new_main():
    print("1 == withdraw money")
    print("2 == deposit money")
    print("3 == view transactions")
    user_input = option_input()
    query(user_input)
    # FIX: removed the extra "do you want to perform another function" question here,
    # because main() already asks it after every new_main() call


main()