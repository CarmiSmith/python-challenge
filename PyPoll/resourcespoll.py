import os
import csv


csvpath = os.path.join('Resources', 'election_data.csv')

    
#giving definition
candidate = {}
candidate_list = []
values = candidate.values()
number_votes = []    
total_votes_cast = 0
candidate_percentage = 0



with open(csvpath) as csvfile:    
    #
    csvreader = csv.reader(csvfile, delimiter=',')
    # removes the header row
    next (csvreader)
    
    

    for row in csvreader:
        #adding up the total votes
        total_votes_cast += 1
        
        #pulling candidates names and calculating their votes
        candidate_name = row[2]
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate[candidate_name] = 1
        #moving on to the next candidate  
        else: 
            candidate[candidate_name] += 1 

    #print my results     
    print(f"Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes_cast}")
    print("-------------------------") 

    #exporting results to text file
    fileoutput = open("Analysis/analysis.txt", "w")
    fileoutput.write(f"Election Results\n")  
    fileoutput.write(f"-------------------------\n") 
    fileoutput.write(f"Total Votes: {total_votes_cast}\n")

    #putting candidates in a list
    for name in candidate_list:
        number_votes = candidate.get(name) 

        #calculating percentage of votes  
        candidate_percentage = ((number_votes /total_votes_cast) * 100)

        #printing my results
        print(f"{name}: {round(candidate_percentage)}% {str(candidate[name])}")

        #exporting results to text file
        fileoutput.write(f"{name}: {round(candidate_percentage)}% {str(candidate[name])}\n")

        #pulling winners name
        winner = max(name, str(candidate[candidate_name]))

    #printing my results
    print("-------------------------")
    print(f"Winner: {winner}")     
    print("-------------------------")   

    #exporting results to text file
    fileoutput.write(f"-------------------------\n")
    fileoutput.write(f"Winner: {winner}\n")
    fileoutput.write(f"-------------------------\n")
    
    


    


  