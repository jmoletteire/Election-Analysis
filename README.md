# Election-Analysis

## Project Overview
A Colorado Board of Elections employee has asked for an election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidate who received votes.
3. Calculate the percentage of votes each candidate won.
4. Calculate the total number of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.68.1

## Summary
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The counties audited were:
  - Jefferson
  - Denver
  - Arapahoe
- The county results were:
  - Jefferson accounted for 10.5% of all votes with 38,855 votes cast.
  - Denver accounted for 82.8% of all votes with 306,055 votes cast.
  - Arapahoe accounted for 6.7% of all votes with 24,801 votes cast.
- The county with the largest turnout was:
  - Denver, which accounted for 82.8% of all votes with 306,055 votes cast.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote with 85,213 votes.
  - Diana DeGette received 73.8% of the vote with 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote with 11,606 votes.
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 votes.

## Statement to Election Commission
The Python script that provided this analysis is capable of providing the same insight for any election at any level. Given a set of voter data (sorted or unsorted), a few tweaks would allow the user to quickly calculate the results, and determine the victor, of any race.

Say we want to determine which candidate won in each county. One solution would involve creating n dictionaries for candidate votes, where n is equal to the number of counties. To do this we could create a dictionary of dictionaries, and each time we came across a new county we would create a new dictionary for it within the larger dictionary that had already been declared. Then we would tally the votes in a method parallel to the one used in this assignment, just with an extra step for finding the right county's dictionary of results.

Assuming the raw data was organized as it was in this assignment (ID, Region, Candidate), we could determine the results of a national election with this script. Using the method described above (but with states in place of counties), we could determine the winning candidate in each state. We could then have a dictionary that contains key-value pairs of state names and electoral college votes, and change our list of candidates to a dictionary of candidates and electoral votes received. As winners in each state were determined, we would simply look up that state's electoral votes in our dictionary, then look up the candidate's name in the other dictionary and increment their votes received by that amount. It may sound like a lot to change, but it would only require a few more lines of code and some more complex data structures.
