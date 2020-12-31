import os
import csv


csvpath = os.path.join('..', 'Resources', 'election_data.csv')
#print (csvpath)
with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    # removes the header row
    next (csvreader)
    for row in csvreader:
       # print(row)

