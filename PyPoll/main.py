import os
import csv

# to refer to csv file
pypoll_data= os.path.join('.','election_data.csv')

    # to open csv file
with open(pypoll_data,'r', newline='') as pypollfile:
    pyPdata_reader= csv.reader(pypollfile, delimiter=',')
    
    votes= []
    candidates= []
    
    for lines in pyPdata_reader:
        # to create a list of the date column
        columns=list(lines)
        votercol= columns[0]
        votes.append(votercol)
        #to create a list of candidates
        candidatescol= columns[2] 
        candidates.append(candidatescol)
    
    #to remove header from data
    votes.pop(0)
    candidates.pop(0)
    #['Li', 'Correy', 'Khan', "O'Tooley"]
    
    #to calculate total num of votes
    tot_votes=len(votes)
    #to calculate % of votes

    print("Election Results")
    print("----------------------")
    print(f"Total Votes: {tot_votes}")
    print("----------------------")

    
    list_candidates=list(set(candidates))
    j = 0
    votevalues= []
    
    while j < 4:
        Total= sum(1 for i in candidates if i == list_candidates[j])
        percent= round((Total/tot_votes) * 100,2)
        print(f"{list_candidates[j]}:{percent}% ({Total})")  
        j = j + 1
        #to create a list of total values
        votevalues.append(Total)
    
    #to get the index for the max value
    maxvotenum= max(votevalues)
    maxvote_ref= int([i for i, j in enumerate(votevalues) if j == maxvotenum][0])
    #to get the candidate per index value
    winner = list_candidates[maxvote_ref]
    
    print("---------------------")
    print(f"Winner: {winner}")
    print("---------------------")

#I would sort the winners from highest to lowest but my soul needs to recover.
# I had alot of breakthroughs with the homeworks, lots of fun!  

    