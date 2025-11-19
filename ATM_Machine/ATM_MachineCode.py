# 🏧 ATM Machine Program (Using While Loop)
balance = 1000  # Starting balance
pin = "1234"

# Step 1: PIN Check
user_pin = input("Enter ATM PIN: ")

while user_pin != pin:
    print("Wrong PIN! Try again.")
    user_pin = input("Enter ATM PIN: ")

print("Login Successful!\n")

# Step 2: ATM Menu
while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")

    # Option 1 → Balance
    if choice == "1":
        print("Your Balance:", balance)

    # Option 2 → Deposit
    elif choice == "2":
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print("Amount Deposited Successfully!")
        print("Updated Balance:", balance)

    # Option 3 → Withdraw
    elif choice == "3":
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Withdraw Successful!")
            print("Remaining Balance:", balance)
        else:
            print("Insufficient Balance!")

    # Option 4 → Exit
    elif choice == "4":
        print("Thank You for using ATM 🙂")
        break

    else:
        print("Invalid Option! Please choose again.")
