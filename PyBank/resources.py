# Resources

import os
import csv

#the path to the information I need to pull
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    
    #these give definition
    total_profit_loss = 0  
    profit_loss_change = []
    profit_loss = []
    date_change = []
    csvreader = csv.reader(csvfile, delimiter=',')

    # removes the header row
    next (csvreader)
    
    for row in csvreader:
       
        #pulls information
        date_change.append(row[0])    
        
        #adds the total number of months
        total_line_count = sum(1 for line in open(csvpath))
        
        #adds the net total of profit/losses over the entire period 
        total_profit_loss = total_profit_loss + int(row[1]) 
        
        #pulls information
        profit_loss.append(row[1])   

for x in range(1, len(profit_loss)):
    #adds the net total of profit/losses over the entire period 
    profit_loss_change.append(int(profit_loss[x])-int(profit_loss[x-1]))

#calculate the changes in Profit/Losses over the entire period and find the average
average_change = round(sum(profit_loss_change)/len(profit_loss_change),2) 

#this sets up the greatest increase in profit
mplchange = max(profit_loss_change)

#this sets up the greatest decrease in profit
nplchange = min(profit_loss_change)

#The greatest increase in profits (date and amount) over the entire period
date_max = date_change[profit_loss_change.index(mplchange)+1]

#The decrease in losses (date and amount) over the entire period
date_min = date_change[profit_loss_change.index(nplchange)+1]

#print all my results       
print(f"Financial Analysis")       
print("-----------------------------")
print(f"Total Months: {total_line_count-1}")
print(f"Total: ${total_profit_loss}") 
print(f"Average Changes: ${average_change}")   
print(f"Greatest Increase in Profits: {date_max} (${mplchange})")
print(f"Greatest Decrease in Profits: {date_min} (${nplchange})")
#exporting results to text file
fileoutput = open("Analysis/analysis.txt","w")
fileoutput.write(f"Financial Analysis\n")
fileoutput.write("-----------------------------\n")
fileoutput.write(f"Total Months: {total_line_count-1}\n")
fileoutput.write(f"Total: ${total_profit_loss}\n")
fileoutput.write(f"Average Changes: ${average_change}\n")
fileoutput.write(f"Greatest Increase in Profits: {date_max} (${mplchange})\n")
fileoutput.write(f"Greatest Decrease in Profits: {date_min} (${nplchange})\n")




        
           
       