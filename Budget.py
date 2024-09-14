import json

def add_expenses(expenses, description, amount):
    expenses.append({"Description": description, "amount": amount})
    print(f"Added expense: {description}, Amount: {amount}")

def get_total_expenses(expenses):
    total = 0
    for expense in expenses:
        total += expense['amount']
    return total

def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses)

def show_budget_details(budget, expenses):
    print(f"Total budget: {budget}")
    print("Expenses:")
    for expense in expenses:
        print(f"> {expense['amount']}: {expense['Description']}")
    print(f"Total Spent: {get_total_expenses(expenses)}")
    print(f"Remaining budget: {get_balance(budget, expenses)}")

def load_budgetdata(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data["initialbudget"], data["expenses"]
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, [] 
    
def save_budget_details(filepath, initial_budget, expenses):
    data = {
        'initial_budget': initial_budget,
        'expenses': expenses
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    filepath = 'budgetdata.json'
    initial_budget, expenses = load_budgetdata(filepath)

    if initial_budget == 0:
            initial_budget = float(input("Please enter your initial budget: "))
    budget = initial_budget
    while True:
        print("\nChoose an option:")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Exit")
        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            description = input("What was this expense?: ")
            amount = float(input("What was the amount of this purchase? $"))
            add_expenses(expenses, description, amount)
        elif choice == "2":
            show_budget_details(budget, expenses)
        elif choice == "3":
            save_budget_details(filepath, budget, expenses)
            print("Exit in progress...")
            break
        else:
            print("Invalid input, please try again")

if __name__ == "__main__":
    main()