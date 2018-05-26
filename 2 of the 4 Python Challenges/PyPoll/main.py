# import file path
import os 
filepath = os.path.join("/Users/abulla/Desktop/python/pandas/USCLOS201805DATA1-Class-Repository-DATA-master/02-Homework/03-Python/Instructions/PyPoll/raw_data/election_data_1.csv")
# Import the csv module
import csv
# use 'collections' module for 'counter' tallies for voting
from collections import Counter

# Read the 'election_data' csv file 
with open(filepath, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    # Avoid the header from the data by using 'next()' function
    next(csvreader, None)
    # list the variables
    voterid = []
    county = []
    candidates = []
    # run the loop and append the rows 
    for row in csvreader:
        voterid.append(row[0]) # 1st col.
        county.append(row[1])  # 2nd col.
        candidates.append(row[2]) # 3rd col.
    # use set() function to collect unique set of candidates
    unique_candidate = set(candidates)
    totalvotes= len(voterid) # find total vote
    # Use the counter() function to count the number of votes for the politicians
    voteCount = Counter(candidates)
    # Create a list of the name of the candidates
    candidate_names = []
    
    for row in unique_candidate:
        candidate_names.append(row)   
    
    print('Election Results' + '\n')
    print('=='*len("Election Results") + '\n')
    print('Total Votes: ' + str(totalvotes) + '\n')
    print('=='*len("Total Votes:") + '\n')
    
    #Now create a dictionary of nested list
    dict_candidate = {}
    candidate_count = 0
    for i in candidate_names:
        cand_name = str(candidate_names[candidate_count]
        vote = candidates.count(cand_name)
        vote = int(vote)
        percentage = round(votes / tot_vote * 100, 2)
        dict_candidate.update({cand_name: votes})
        print('{cand_name}: {percentage}% ({votes} votes' + '\n')
        candidate_count = candidate_count + 1
        
        winner = max(dic_candidate, key=lambda key: dic_candidate[key])
        print("Winner: ", winner)
