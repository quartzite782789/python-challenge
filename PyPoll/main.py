# -*- coding: UTF-8 -*-
"""PyPoll CThomas Solution"""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
c=0 #Store current row's candidate name
perc=0  #Calculate a candidate's percentage of votes

# Define lists and dictionaries to track candidate names and vote counts
candidates={}   #Dictionary of candidates and their respective votes

# Winning Candidate and Winning Count Tracker
win=0   #Winning vote count
winc="N/A"  #Winning candidate

# Print variables
ptotal_votes="N/A"  #String variable to store the print/write output of the total votes summary
pcandidates="N/A"   #String variable to store the print/write output of the candidate summary
pwin="N/A"  #String variable to store the print/write output of the winner summary

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes =total_votes+1

        # Get the candidate's name from the row
        c=row[2]    #Store current row Candidate name

        # If the candidate is not already in the candidate list, add them
        if c not in candidates:
            candidates[c]=1 #Add key "c" and set value (vote count) to 1

        # Add a vote to the candidate's count
        else:
            candidates[c]=candidates.get(c)+1   #Increment the value (vote count) of c (current row candidate) by 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal).
    ptotal_votes=f"\nElection Results\n-------------------------\nTotal Votes: {total_votes}\n-------------------------\n"
    print(ptotal_votes)

    # Write the total vote count to the text file
    txt_file.write(ptotal_votes)

    # Loop through the candidates to determine vote percentages and identify the winner
    for key, value in candidates.items():   #Loop through the dictionary for each key/value pair

        # Get the vote count and calculate the percentage
        perc=round(value*100/total_votes,3)     #Calculate percentage, calling value for the vote count
        pcandidates=f"{key}: {perc}% ({value})\n"

        # Update the winning candidate if this one has more votes
        if win<value:   #If current value (vote count) is larger than previously stored max, store it and the key (candidate)
            win=value
            winc=key

        # Print and save each candidate's vote count and percentage
        print(pcandidates)
        txt_file.write(pcandidates)

    # Generate and print the winning candidate summary
    pwin=f"-------------------------\nWinner: {winc}\n-------------------------\n"
    print(pwin)

    # Save the winning candidate summary to the text file
    txt_file.write(pwin)