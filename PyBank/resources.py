# Resources

import os
import csv

csvpath = os.path.join('..', 'but-ind-data-pt-12-2020-u-c', 'Week-03-Python', 'Homework', 'Instructions', 'PyBank', 'Resources', 'budget_data.csv')
print (csvpath)
with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    next (csvreader)
    for row in csvreader:
    

