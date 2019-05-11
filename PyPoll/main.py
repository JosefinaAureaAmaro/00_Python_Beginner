import os
import csv

# to refer to csv file
pypoll_data= os.path.join('.','election_data.csv')

    # to open csv file
with open(pypoll_data,'r', newline='') as pypollfile:
    pyPdata_reader= csv.reader(pypollfile, delimiter=',')
    
    #variables for list by column
    votes= []
    candidates= []
    
    for lines in pyPdata_reader:
        # to create a list of the votes column
        columns=list(lines)
        votercol= columns[0]
        votes.append(votercol)
        #to create a list of candidates
        candidatescol= columns[2] 
        candidates.append(candidatescol)
    
    #to remove header from data
    votes.pop(0)
    candidates.pop(0)
    
    #to calculate total num of votes
    tot_votes=len(votes)
    
    #print first set of a format and statements
    print("Election Results")
    print("----------------------")
    print(f"Total Votes: {tot_votes}")
    print("----------------------")

    #variables for while loop below
    list_candidates=list(set(candidates))
    j = 0 #j is the loop variable for the list_candidates 
    votevaluespercand= [] #to create a list of the total votes per candidate


    #to loop thorough the candidate column and the list of candidates to calculate total votes per Candidate and % of votes per candidate
    while j < 4:
        #total 1 for every time the candidates name occures in the candidate column = totalvotesper candidate
        Totalvotespercan= sum(1 for i in candidates if i == list_candidates[j]) 
        percentpercan= round((Totalvotespercan/tot_votes) * 100,2)
        #print list of candidates, percentofvotespercan & totalvotespercan
        print(f"{list_candidates[j]}:{percentpercan}% ({Totalvotespercan})")  
        j = j + 1
        #to create a list of total votes per candidates produced
        votevaluespercand.append(Totalvotespercan)
        #the total votes per candidate come out with the same index value as the ordered list of candidates

    #to get the index value of the vote values per candidate list:
    #to get the index of the max value
    maxvotenum= max(votevaluespercand)
    maxvote_ref= int([i for i, j in enumerate(votevaluespercand) if j == maxvotenum][0])
    #to get the candidate per the max index value
    winner = list_candidates[maxvote_ref]
    
    print("---------------------")
    print(f"Winner: {winner}")
    print("---------------------")

#I would sort the winners from highest to lowest but my soul needs to recover.
#I had alot of breakthroughs, debug, and concepts clicked with the python challenges.Lots of fun!  :D

    