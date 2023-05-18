# PyBank
# analyze records to calculate 
    #total number of months
    #net total amount of profit/losses
    # greatest increase in profits (date and amount)
    # greatest decrease in profits (date and amount)

import csv
import os

#set path to input file
file_path = os.path.join("Resources", "budget_data.csv")

#initialize variables
total_months = 0
net_total = 0
prof_change = []
g_inc = ['',0]
g_dec = ['',0]
previous_profit = 0

#read csv file
with open(file_path) as csvfile:
    csv_reader = csv.reader(csvfile)
    #skip header row
    header = next(csv_reader)
    
    #read each row of the file
    for row in csv_reader:
        #count the number of months
        total_months = total_months + 1
        #get the date and profit loss
        date = row[0]
        profit = int(row[1])
        #calculate sum of all rows
        net_total = net_total + profit
        change = profit - previous_profit
        #check if the change is greatest increase or decrease
        if total_months > 1:
            prof_change.append(change)
        if change > g_inc[1]:
            g_inc = [date, change]
        elif change < g_dec[1]:
            g_dec = [date, change]
        previous_profit = profit

#calculate average month to month change
avg_change = sum(prof_change)/len(prof_change)
        

report = f'''
Financial Analysis
---------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${avg_change:.2f}
Greatest Increase in Profits: {g_inc[0]} (${g_inc[1]})
Greatest Decrease in Profits: {g_dec[0]} (${g_dec[1]})
'''
print(report)
output_path = os.path.join("analysis","financial_analysis.txt")
with open(output_path, "w") as outputfile:
    outputfile.write(report)