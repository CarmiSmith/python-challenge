import os
import csv


csvpath = os.path.join('Resources', 'election_data.csv')
#print (csvpath)
with open(csvpath) as csvfile:
    
    #giving definition
    votes_cast = []
    total_votes_cast = 0
    

    csvreader = csv.reader(csvfile, delimiter=',')
    # removes the header row
    next (csvreader)
    for row in csvreader:
       #print(row)

       
       total_votes_cast = sum(1 for lines in open(csvpath))
       candidate_list = (row[2])


print(f"Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes_cast-1}")
print("-------------------------")
print(candidate_list)
