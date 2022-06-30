import csv
import os

# Load/Save variables
fileToLoad = os.path.join("Resources","election_results.csv")
fileToSave = os.path.join("Analysis","election_analysis.txt")

totVotes = 0

# Candidates
candidates = []
votes = {}
winner = ""
winCount = 0
winPercent = 0

# Counties
counties = []
countyVotes = {}
largestTurnout = ""
largestCount = 0
largestPercent = 0

# Open election results and read
with open(fileToLoad, "r") as electionData:
    fileReader = csv.reader(electionData)

    # read headers
    headers = next(electionData)

    # read csv
    for row in fileReader:
        totVotes += 1
        name = row[2]
        county = row[1]

        # add name to list of candidates (if needed)
        if name not in candidates:
            candidates.append(name)
            votes[name] = 0
        
        # add county to list (if needed)
        if county not in counties:
            counties.append(county)
            countyVotes[county] = 0

        # add vote
        votes[name] += 1
        countyVotes[county] += 1

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

    # Print each county's voter count and percentage
    print("\nCounty Votes:\n")
    txt_file.write("\nCounty Votes:\n")

    for county in counties:
        perVote = countyVotes[county] / totVotes * 100

        # determine largest percentage and largest vote count
        if (countyVotes[county] > largestCount) and (perVote > largestPercent):
            largestTurnout = county
            largestCount = countyVotes[county]
            largestPercent = perVote
        
        # calculate county results
        countyResults = (
            f"{county}: {perVote:.1f}% ({countyVotes[county]:,})\n")

        print(countyResults)
        txt_file.write(countyResults)

    turnoutSummary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largestTurnout}\n"
        f"-------------------------\n")
    print(turnoutSummary)
    txt_file.write(turnoutSummary)

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