# The data we need to retrieve:
# 1. The total number of votes cast
# 2. A complete list of candidate who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os

# Load/Save variables
fileToLoad = os.path.join("Resources","election_results.csv")
fileToSave = os.path.join("Analysis","election_analysis.txt")

totVotes = 0
candidates = []
votes = {}
winner = ""
winCount = 0
winPercent = 0

# Open election results and read
with open(fileToLoad, "r") as electionData:
    fileReader = csv.reader(electionData)

    # read headers
    headers = next(electionData)

    # read csv
    for row in fileReader:
        totVotes += 1
        name = row[2]

        # add name to list of candidates (if needed)
        if name not in candidates:
            candidates.append(name)
            votes[name] = 0
        
        # add vote
        votes[name] += 1

for name in candidates:
    perVote = votes[name] / totVotes * 100
    print(f"{name}: {perVote:.1f}% ({votes[name]:,})\n")

    if (votes[name] > winCount) and (perVote > winPercent):
            winner = name
            winCount = votes[name]
            winPercent = perVote

winnerSummary = (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"Winning Vote Count: {winCount:,}\n"
    f"Winning Percentage: {winPercent:.1f}%\n"
    f"-------------------------\n")
print(winnerSummary)