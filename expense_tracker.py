"""A small console-based expense tracker."""

from pathlib import Path


DATA_FILE = Path(__file__).with_name("expenses.txt")


class Expense:
    def __init__(self, amount, category, note):
        self.amount = amount
        self.category = category
        self.note = note

    def show(self, number):
        print(
            f"{number}. {self.category} - "
            f"{self.note} - Rs. {self.amount:.2f}"
        )


def load_expenses():
    expenses = []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    amount_text, category, note = line.rstrip("\n").split("|", 2)
                    amount = float(amount_text)
                    if amount <= 0 or not category or not note:
                        raise ValueError
                except ValueError:
                    print(f"Skipping invalid record on line {line_number}.")
                    continue

                expenses.append(Expense(amount, category, note))
    except FileNotFoundError:
        return expenses
    except OSError as error:
        print(f"Could not read expense records: {error}")
        return None

    return expenses


def read_required_text(prompt):
    while True:
        value = input(prompt).strip()
        if value and "|" not in value:
            return value
        print("Enter a value without the | character.")


def read_amount():
    while True:
        try:
            amount = float(input("Amount (Rs.): "))
        except ValueError:
            print("Please enter a number.")
            continue

        if amount > 0:
            return amount
        print("Amount must be greater than zero.")


def add_expense(expenses):
    amount = read_amount()
    category = read_required_text("Category: ")
    note = read_required_text("Note: ")
    expense = Expense(amount, category, note)

    try:
        with DATA_FILE.open("a", encoding="utf-8") as file:
            file.write(
                f"{expense.amount}|{expense.category}|{expense.note}\n"
            )
    except OSError as error:
        print(f"Could not save expense: {error}")
        return

    expenses.append(expense)
    print("Expense added.")


def show_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- Your Expenses ---")
    for number, expense in enumerate(expenses, start=1):
        expense.show(number)


def show_total(expenses):
    total = 0
    for expense in expenses:
        total += expense.amount
    print(f"Total expenses: Rs. {total:.2f}")


def main():
    expenses = load_expenses()
    if expenses is None:
        return

    while True:
        print(
            "\n=== Expense Tracker ===\n"
            "1. Add an expense\n"
            "2. View expenses\n"
            "3. Show total\n"
            "0. Exit"
        )
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Choose 0-3.")


if __name__ == "__main__":
    main()
