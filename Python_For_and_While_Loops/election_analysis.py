# Dependancies
import os
import csv

# CSV File with os
pypoll_data= os.path.join('.','election_data.csv')

# to read csv file
with open(pypoll_data,'r', newline='') as pypollfile:
    poll_data_reader = csv.reader(pypollfile, delimiter=',')
    
    #variables for list by column
    votes= []
    candidates= []
    
    for rows in poll_data_reader:
        # store the data of the csv into a list
        columns = list(rows)

        # store the voter data into a list
        votercol = columns[0]
        votes.append(votercol)


        # store the candidate data into a list
        candidatescol= columns[2] 
        candidates.append(candidatescol)
    
    # to remove header from data
    votes.pop(0)
    candidates.pop(0)
    
    # to calculate total num of votes
    tot_votes= len(votes)

    # variables for while loop below

    # to create a list of candidates without duplicates
    list_candidates = list(set(candidates))


    ########## while loop ####################


    i = 0 # i is the loop variable for the list_candidates 

    candidate_vote_tally = [] # to create a list of the total votes per candidate
    tally_results = [] # to create a list of the final results for candidate

    # Objectives: 
    # 1. To loop thorough the candidate column and the list of candidates to calculate total votes per Candidate
    # 2. Calculate the % of votes per candidate


    while i < len(list_candidates):

        # (Boolean) total votes per candidate =  count the number of times the candidate name appears in the column by adding 1 for each True conditon
        total_votes_per_candidate = sum( 1 for x in candidates if x == list_candidates[i]) 
        percent_votes_per_candidate = round((total_votes_per_candidate / tot_votes) * 100,2)
        #print list of candidates, percentofvotespercan & totalvotespercan
        results_output = (f"{list_candidates[i]}:{percent_votes_per_candidate}% ({total_votes_per_candidate})")

        # to create a list of total votes per candidates produced
        ## the total votes per candidate come out with the same index value as the ordered list of candidates
        candidate_vote_tally.append(total_votes_per_candidate)
        tally_results.append(results_output)
        
        i += 1

    ########## vote analysis ####################

    # To get the result of the winning candidate

    # to get the index of the max voter
    winning_votes_index = candidate_vote_tally.index(max(candidate_vote_tally))
    # to get he name of winning candidate
    winner = list_candidates[winning_votes_index]
   
    # format candidate results for text file 
    ## used candidate names as variables for final results
    khan_results = (str(tally_results[0]))
    correy_results = (str(tally_results[1]))
    tooley_results = (str(tally_results[2]))
    li_results = (str(tally_results[3]))
    #example of print out for tally_results: ['Khan:63.09% (661583)', 
    #                                         'Correy:19.94% (209046)',
    #                                         "O'Tooley:3.01% (31586)",
    #                                         'Li:13.96% (146360)']
    
    # final voting results 
    election_results =(f"""Election Results\n
                  ----------------------\n
                  Total Votes: {tot_votes}\n
                  ----------------------\n
                  {khan_results}\n
                  {correy_results}\n
                  {li_results}\n
                  {tooley_results}\n
                  ---------------------\n
                  Winner: {winner}
                  \n---------------------""")
    
print(election_results)

#------to print election results to a txt file----------------
import sys 

election_results_txt_path = os.path.join('.','election_results.txt')
with open(election_results_txt_path,'w') as election_txt_file:
    sys.stdout = election_txt_file
    
    print(election_results)

