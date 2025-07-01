import sys

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("=== Welcome to the Budgeting Tool ===\n")
    print("This tool will help you track your income, expenses, and savings goals.\n")
    print("You will be asked to enter your monthly income, then the number of expense items you want to track, and finally your savings goal.\n")

    income = get_float("Enter your total monthly income: $")

    # Ask for number of expenses
    while True:
        try:
            num_expenses = int(input("How many different expense items do you want to enter? "))
            if num_expenses < 0:
                print("Please enter a non-negative number.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    expenses = []
    if num_expenses == 0:
        print("No expenses to enter.")
    else:
        print("\nNow, enter each expense name and amount.")
        for i in range(1, num_expenses + 1):
            while True:
                name = input(f"Expense #{i} name: ").strip()
                if name:
                    break
                print("Expense name cannot be empty.")
            amount = get_float(f"Amount for {name}: $")
            expenses.append((name, amount))

    total_expenses = sum(amount for _, amount in expenses)

    savings_goal = get_float("\nEnter your monthly savings goal: $")

    print("\n=== Budget Summary ===")
    print(f"Total Income:     ${income:.2f}")
    print(f"Total Expenses:   ${total_expenses:.2f}")
    print(f"Savings Goal:     ${savings_goal:.2f}")
    remaining = income - total_expenses - savings_goal
    print(f"Remaining Budget: ${remaining:.2f}")

    if remaining < 0:
        print("Warning: You are over budget! Consider reducing expenses or savings goal.")
    else:
        print("Great job! Your budget is balanced.")

    if expenses:
        print("\nExpense Breakdown:")
        for name, amount in expenses:
            print(f"- {name}: ${amount:.2f}")
    else:
        print("\nNo expenses entered.")

    print("\nThank you for using the Budgeting Tool!")

if __name__ == "__main__":
    main() 