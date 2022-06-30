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

# Write results to file
with open(fileToSave, "w") as txt_file:
    # Print and save final vote count
    electionResults = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {totVotes:,}\n"
        f"-------------------------\n")
    print(electionResults)
    txt_file.write(electionResults)

    # Print each candidate's voter count and percentage
    for name in candidates:
        perVote = votes[name] / totVotes * 100

        # determine winning percentage, winning vote count, and winner
        if (votes[name] > winCount) and (perVote > winPercent):
            winner = name
            winCount = votes[name]
            winPercent = perVote
        
        # calculate candidate results
        candidateResults = (
            f"{name}: {perVote:.1f}% ({votes[name]:,})\n")
        
        # print candidate results to terminal
        print(candidateResults)

        # save candidate results to file
        txt_file.write(candidateResults)

    # Print winning candidate's results to terminal
    winnerSummary = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"Winning Vote Count: {winCount:,}\n"
        f"Winning Percentage: {winPercent:.1f}%\n"
        f"-------------------------\n")
    print(winnerSummary)

    # Save winning candidate's results to file
    txt_file.write(winnerSummary)