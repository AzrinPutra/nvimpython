def add_expense():
    # Get valid expense name
    expense_name = ""  # Created a variable with an empty string
    while not expense_name:
        expense_name = input("Enter expense name: ")
        if not expense_name:
            print("Expense name cannot be empty")

    # Get valid amount
    expense_amount = None
    while expense_amount is None:
        try:
            expense_amount = float(input("Enter expense amount: "))
            if expense_amount <= 0:
                print("Expense amount cannot be negative")
                expense_amount = None
        except ValueError:
            print("Error: Please enter a valid expense amount")

    # Saving logic
    with open("expenses.txt", "a") as f:
        f.write(f"{expense_name}: ${expense_amount:.2f}\n")

    print(f"{expense_name}: ${expense_amount:.2f} has been added successfully")


def view_expenses():
    try:
        with open("expenses.txt", "r") as f:
            expenses = f.readlines()
            for line in expenses:
                print(f"{line}")
    except FileNotFoundError:
        print("File not found")


def main():

    while True:
        print("1. Add expense")
        print("2. View expenses")
        print("3. Exit")

        choice = input("Choose your option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Invalid choice")
