# import file path
import os 
election_file = os.path.join('##')
# Import the csv module
import csv
# use 'collections' module for 'counter' tallies for voting
from collections import Counter

# Read the 'election_data' csv file 
with open(election_file, 'r', newline='') as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter= ',')
    # Avoid the header from the data by using 'next()' function
    next(csvReader, None)
    
    # list the variables
    voterid = []
    county = []
    candidates = []
    # append the rows 
    for row in csvReader:
        voterid.append(row[0]) # 1st col.
        county.append(row[1])  # 2nd col.
        candidates.append(row[2]) # 3rd col.
    # use set() fuction to collect unique set of candidates
    uniqueCand = set(candidates)
    totalvotes= len(voterid)
    # Use the counter() function to count the number of votes for the politicians
    voteCount = Counter(candidates)
    # List the name of the candidates
    candidateNames = []
    for row in uniqueCand:
        candidateNames.append(row)
    print("Election Results" + "\n")
    print("--"*len("Election Results") + "\n")
    print("Total Votes: " + str(totalvotes) + "\n")
    print("--"*len("Total Votes:") + "\n")
    
