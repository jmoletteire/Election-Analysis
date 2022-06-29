# The data we need to retrieve:
# 1. The total number of votes cast
# 2. A complete list of candidate who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
with open('Resources/election_results.csv') as electionData:
    print(electionData)
