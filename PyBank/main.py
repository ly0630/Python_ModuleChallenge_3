import os
import csv

def load_csv(file_path):
    with open(file_path, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        header = next(csvreader)
        data = [row for row in csvreader]
    return header, data

def calculate_metrics(data):
    total_months = len(data)
    total_prolss = sum(int(row[1]) for row in data)

    dates = [row[0] for row in data]
    profits = [int(row[1]) for row in data]

    changes = [profits[i] - profits[i - 1] for i in range(1, total_months)]
    average_chg = sum(changes) / len(changes)

    max_increase = max(changes)
    max_index = changes.index(max_increase)
    max_date = dates[max_index + 1]

    max_decrease = min(changes)
    decreased_index = changes.index(max_decrease)
    decreased_date = dates[decreased_index + 1]

    return total_months, total_prolss, average_chg, max_date, max_increase, decreased_date, max_decrease

def print_results(total_months, total_prolss, average_chg, max_date, max_increase, decreased_date, max_decrease):
    print("Financial Analysis")
    print("---------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_prolss}")
    print(f"Average Change: ${round(average_chg, 2)}")
    print(f"Greatest Increase in Profits: {max_date} (${max_increase})")
    print(f"Greatest Decrease in Profits: {decreased_date} (${max_decrease})")

def export_to_txt(output_file_path, total_months, total_prolss, average_chg, max_date, max_increase, decreased_date, max_decrease):
    with open(output_file_path, "w") as output:
        output.write(f'''
Financial Analysis
---------------------
Total Months: {total_months}
Total: ${total_prolss}
Average Change: ${round(average_chg, 2)}
Greatest Increase in Profits: {max_date} (${max_increase})
Greatest Decrease in Profits: {decreased_date} (${max_decrease})
''')

def main():
    file_to_load = os.path.join("budget_data.csv")
    header, data = load_csv(file_to_load)

    total_months, total_prolss, average_chg, max_date, max_increase, decreased_date, max_decrease = calculate_metrics(data)

    print_results(total_months, total_prolss, average_chg, max_date, max_increase, decreased_date, max_decrease)

    output_file_path = "output_PyBank.txt"
    export_to_txt(output_file_path, total_months, total_prolss, average_chg, max_date, max_increase, decreased_date, max_decrease)

if __name__ == "__main__":
    main()
