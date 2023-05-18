#module 3 challange
#PyPoll

#analyze csv and pull data set composed of 
#3 columns (voter ID, County, and candidate)
#to provide summary of total candidate votes, 
#percent & votes by candidate, and winner based on popular vote

import csv
import os

#set path to input file
file_path = os.path.join("Resources", "election_data.csv")

# initialize variables
total_votes = 0
candidates = {}
winner = ""

#read csv
with open(file_path) as csvfile:
    csv_reader = csv.reader(csvfile)
    #skip header row
    header = next(csv_reader)

    #process each row
    for row in csv_reader:
        #increment number of votes
        total_votes = total_votes + 1
        #get the candidates name
        current_can = row[2]
        #add candidates not already in dictionary
        if current_can not in candidates:
            candidates[current_can] = 1
        else: 
            #add vote to current candidate
            candidates[current_can] += 1

#pick winner based on popular vote
#key tells max to look up by vote
#max returns name of candidate with most votes
winner = max(candidates, key = candidates.get)

report = f'''
Election Results
--------------------------
Total Votes: {total_votes}
--------------------------
'''
#calculate percent vote for every candidate
#append to report
for current_can, votes in candidates.items():
    percent_votes = votes / total_votes * 100
    report += f'{current_can}: {percent_votes:.3f}% ({votes})\n'

#append winner to report
report += f'--------------------------\nWinner: {winner}\n--------------------------' 
print(report)

#export report as a text file
output_path = os.path.join("analysis","election_analysis.txt")
with open(output_path, "w") as outputfile:
    outputfile.write(report)
