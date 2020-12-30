import os
import csv


csvpath = os.path.join('..', 'but-ind-data-pt-12-2020-u-c', 'Week-03-Python', 'Homework', 'Instructions', 'PyPoll', 'Resources', 'election_data.csv')
#print (csvpath)
with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    # removes the header row
    next (csvreader)
    for row in csvreader:
        print(row)
        
break