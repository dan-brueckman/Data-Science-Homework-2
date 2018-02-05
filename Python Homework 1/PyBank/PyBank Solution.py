import os
import csv
import locale
locale.setlocale( locale.LC_ALL, '' )
csv_path = os.path.join(".", "budget_data_1.csv")
with open(csv_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    rev_list = []
    date_list = []
    month_count = 0
    revenue = 0
    for row in csvreader:
        month_count += 1
        revenue += float(row[1])
        rev_list.append(float(row[1]))
        date_list.append(row[0])
    high_rev = max(rev_list)
    low_rev = min(rev_list)
    for x in rev_list:
        if x == high_rev:
            high_index = rev_list.index(x)
        elif x == low_rev:
            low_index = rev_list.index(x)
    high_date = date_list[high_index]
    low_date = date_list[low_index]
    avg_rev_change = revenue/month_count
high_money = locale.currency(high_rev, grouping=True)
low_money = locale.currency(low_rev, grouping=True)
total_money = locale.currency(revenue, grouping=True)
avg_money = locale.currency(avg_rev_change, grouping=True)

print("Financial Analysis")
print("------------------")
print("Total Months: " + str(month_count))
print("Total Revenue: " + str(total_money))
print("Average Revenue Change: " + str(avg_money))
print("Greatest Increase in Revenue: " + str(high_date) + " - " + str(high_money))
print("Greatest Decrease in Revenue: " + str(low_date) + " - " + str(low_money))
