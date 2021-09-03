#The data we need to retreive
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of election based on popular vote.
#----------------------------------------------------
# import datetime
# now=datetime.datetime.now()
# print("Time:",now)  

import csv
import os

# Assign a varaiable to load a file from path
file_to_load=os.path.join('Resources','election_results.csv')
# Assign a variable to save a file to path
file_to_save=os.path.join('Analysis','election_results.txt')

# Initialize a total vote counter.
total_votes=0

# Candidate list options
candidate_options=[]
# Declare empty dictonary for all candidates and their votes
candidate_votes={}
# Winning candidate's req
winning_candidate=""
winning_votes=0
winning_percentage=0

# Open the election_results and read the file
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)
    
    # Read the header row
    headers=next(file_reader)
    print(headers)

    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count.
        total_votes+=1

        # Print the candidate name for each row
        candidate_name=row[2] 

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #Add the candidate to the list
            candidate_options.append(candidate_name)
            #Track candidate's vote count
            candidate_votes[candidate_name]=0
        #Add a vote to that candidate's count
        candidate_votes[candidate_name]+=1
    # Print candidate vote dictionary
    print(candidate_votes)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list
    for candidate_name in candidate_votes:
        # Retreive vote count for each candidate
        votes=candidate_votes[candidate_name]
        # calculate vote percentage
        vote_percentage=float(votes)/float(total_votes)*100
        # Print each candidate, their voter count, and percentage
        print(f"{candidate_name} : {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_votes) and (vote_percentage > winning_percentage):
            winning_votes=votes
            winning_percentage=vote_percentage
            winning_candidate=candidate_name

    # Print the winning candidates' results 

    winning_candidate_summary = (
        f"--------------------------------------\n"
        f"Winner : {winning_candidate}\n"
        f"Winning Vote Count : {winning_votes:,}\n"
        f"Winning Percentage : {winning_percentage:.1f}%\n"
        f"--------------------------------------\n")
    print(winning_candidate_summary)



        




