print("Welcome to Personal Expense Tracker!")

expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Total Expense")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount in rupees: "))

        expenses.append(amount)
        print(name, "added successfully!")

    elif choice == "2":
        print("Total Expense: Rs.", sum(expenses))

    elif choice == "3":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
