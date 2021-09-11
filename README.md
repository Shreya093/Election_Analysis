# Election_Analysis

## Project Overview

A Colorado Board of Elections employee has assigned the below tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on the popular vote.

## Resources

- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code , 1.38.1

## Election-Audit Results

The analyis of the election shows that :

 * There were 369,771 votes caste in the elction.
 
 * The candidates were :
 
    * Charles Casper Stockham
    * Diana DeGette
    * Raymon Anthony Doane
    
* The candidate results were:
    
    * Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    * Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    * Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
    
* The winner of the election was :
    
    * Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.
    
* The voter turnout for each county was :

    * Jefferson produced 10.5% of voters, for a total of 38,855 voters.
    * Denver produced 82.8 % of voters, for a total of 306,055 voters.
    * Arapahoe produced 6.7% of voters, for a total of 24,801 voters.
    
* The county with the largest turnout was :

    * Denver, which produced 82.8 % of voters, for a total of 306,055 voters.
    
    <img width="370" alt="election_results_snapshot" src="https://user-images.githubusercontent.com/88418201/132911085-a322b139-a0a8-4965-9615-6faf5a566fee.png">
    
    ## Election-Audit Summary
    
    This script can be used for multiple purposes by having it run  multiple tasks to get a deeper understadning if someone was a campaign manager for a candidate. A little time invested into customizing the script can provide on-demand analysis for years to come.
    
    Some of the examples could be :
    
    Modifying our code to produce turnout results by county is just one of many ways that minor adjustments to the code can reveal critical data. Like we can determine what percentage of each county voted for each candidate by adding an if-statement to the code. These type of Decision Statements are how the code runs calculations and all we've done is provide it with a data file.
    Also, if this would have been a federal election we could have modified our script to determine the vote counts and percentages of states rather than just the county.
    We can also modify our script for future use if there comes any requirement which needs to determine the winning candidate and the number of votes of each candidate by their age or ethnicity so that for the voters it becomes more significant to understand which group they need to appeal to more and cast their votes.
    
   Inorder to summarize,  no matter the number of candidates or counties, the script used to perform the Election Audit can be a valuable resourse for the electoral board.
