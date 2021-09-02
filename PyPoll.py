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

#Assign a varaiable to load a file from path
file_to_load=os.path.join('Resources','election_results.csv')
#Assign a variable to save a file to path
file_to_save=os.path.join('Analysis','election_results.txt')
#Open the election_results and read the file
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)
#Print headers
    headers=next(file_reader)
    print(headers)
    # for row in file_reader:
        # print(row)
        


