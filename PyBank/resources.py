# Resources

import os
import csv


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

        #adds the net total of profit/losses over the entire period
        h = open(csvpath)
        content = h.readlines()
        total_profit_loss = 0
        for line in csvreader:
            for i in line:
                if i.isdigit() == True:
                    total_profit_loss += int(i)
        print(f"Total: ${total_profit_loss}")

        #calculate the changes in Profit/Losses over the entire period and find the average    
        file = open(csvpath)
        def average(numbers):
            length = len(numbers)
            total = 0.0
            for number in numbers:
                total += number
            return total / length
        print(f"Average Change: {average}")
       
       
        #The greatest increase in profits (date and amount) over the entire period
        #The decrease in losses (date and amount) over the entire period    
        import pandas as pd
        df=pd.read_csv(csvpath)
        p=df['Profit/Losses'].max()
        q=df['Profit/Losses'].min()
        print(f"Greatest Increase in Profits: ${p}")
        print(f"Greatest Decrease in Profits: ${q}")

       
        break
