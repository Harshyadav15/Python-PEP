# ATM simulator

file_name = "atm_data.txt"

# balance is a global variable that stores money
balance = 1000
pin = "1234"  # global variable that stores atm pin

# load data function
def load_data():
    global balance, pin  # global keyword allow us to modify outside variable
    try:
        # open the file in read mode
        file = open(file_name, "r")
        # read all lines from the file into a list            
        lines = file.readlines()
        # close the file after reading
        file.close()
        # first line contains pin, strip removes
        pin = lines[0].strip()
        # second line contains balance
        balance = int(lines[1].strip())
    except:
        # if file doesn't exist or error occurs
        # pass means "do nothing "
        # program will use defult balance and pin
        pass

# check balance
def check_balance():
    print("your balance is:", balance)

# saved data
def save_data():
    # openining a file in write mode
    file = open(file_name, "w")
    # write a pin into the file and go next line
    file.write(pin + "\n")
    # write abalance as string
    file.write(str(balance))
    # close the file
    file.close()

# deposit money
def deposit_money():
    # global allows us to changing original balance
    global balance
    try:
        amount = int(input("enter amount of deposit:"))
        balance = balance + amount
        # save updated balance to the file
        save_data()
        print("money deposited successfully")
    except:
        print("please enter numbers only")

# withdraw money
def withdraw_money():
    global balance
    try:
        amount = int(input("enter the amount u want to withdraw:"))
        if amount > balance:
            print("insufficient balance!")
        else:
            balance = balance - amount
            save_data()
            print("please collect ur cas !!!")
    except:
        print("please enter number only")

# change pin
def change_pin():
    global pin
    # ask user for old pin
    old_pin = input("enter old pin ")
    # check if old pin matches
    if old_pin == pin:
        # ask for new pin
        new_pin = input("enter ur new pin :")
        pin = new_pin
        save_data()
        print("pin changed succesfully")
    else:
        print("incorrect pin")

# Main program
def main():
    # load data when program starts
    load_data()
    # ask user to enter a pin
    user_pin = input("enter the pin:")
    # if pin is wrong stop the program
    if user_pin != pin:
        print("incorrect pin ")
        return

    while True:
        print("\n-----ATM menu-------")
        print("1.check balance")
        print("2.Deposit money")
        print("3.withdraw money")
        print("4.change pin")
        print("5.Exit")

        choice = input("enter ur choice:")
        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            change_pin()
        elif choice == "5":
            print("thank you for using atm")
            break

main()
