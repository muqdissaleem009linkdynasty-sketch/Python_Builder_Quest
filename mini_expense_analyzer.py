expenses = [250, 400, 120, 600, 300]


def get_total(expenses):
    total = 0

    for expense in expenses:
        total += expense

    return total


def show_large_expenses(expenses, limit):
    print(f"Expenses above {limit}:")

    for expense in expenses:
        if expense > limit:
            print(expense)


total = get_total(expenses)

print(f"Total expense: {total}")

limit = int(input("Enter expense limit: "))

show_large_expenses(expenses, limit)