# Resources

import os
import csv

Total_Month = []
Total = []
Average_Change = []
Greatest_Increase = []
Greatest_Decrease = []

csvpath = os.path.join('..', 'but-ind-data-pt-12-2020-u-c', 'Week-03-Python', 'Homework', 'Instructions', 'PyBank', 'Resources', 'budget_data.csv')
#print (csvpath)
with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    # removes the header row
    next (csvreader)
    for row in csvreader:
        #print(row)

        
        #adds the total number of months
        total_line_count = sum(1 for line in open(csvpath))
        print(f"Total Months: {total_line_count}")       

        #adds the net total
        h = open(csvpath)
        content = h.readlines()
        total_profit_loss = 0
        for line in content:
            for i in line:
                if i.isdigit() == True:
                    total_profit_loss += int(i)
        print(f"Total: {total_profit_loss}")

    #calculate the changes in Profit/Losses and find the average    
        file = open(csvpath)
        def average(numbers):
            length = len(numbers)
            total = 0.0
            for number in numbers:
                total += number
            return total / length
        print(f"Average Change: {average}")
        
        break
