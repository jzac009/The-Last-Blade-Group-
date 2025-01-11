import csv
from datetime import datetime

# Function to log an expense into a CSV file
def log_expense(amount, category, description):
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        # Writing the expense data with the current date and time
        writer.writerow([datetime.now(), amount, category, description])

# Function to generate a report of all logged expenses
def generate_report():
    total = 0
    # Reading the expenses from the CSV file
    try:
        with open('expenses.csv', 'r') as file:
            reader = csv.reader(file)
            # Iterating over each row and summing the expenses
            for row in reader:
                total += float(row[1])  # Adding the amount (second column)
        # Printing the total expenses
        print(f'Total Expenses: ${total:.2f}')
    except FileNotFoundError:
        print("No expense data found. Please log some expenses first.")

# Usage of logging and generating a report
log_expense(50, 'Groceries', 'Bought fruits and vegetables')
log_expense(30, 'Entertainment', 'Cinema tickets')
generate_report() #Reads all logged expenses from the CSV file and calculates the total
