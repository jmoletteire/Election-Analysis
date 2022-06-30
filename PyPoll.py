# The data we need to retrieve:
# 1. The total number of votes cast
# 2. A complete list of candidate who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os

fileToLoad = os.path.join("Resources","election_results.csv")
fileToSave = os.path.join("Analysis","election_analysis.txt")

with open(fileToLoad, "r") as electionData:
    fileReader = csv.reader(electionData)

    headers = next(electionData)
    print(headers)