<div align="center">
<img src="https://github.com/JosefinaAureaAmaro/00_Python_Beginner/blob/master/images/github_repo_header_img.PNG">
</div>
<h2> Repository Details </h2>
<div>
  <p><b>Data Source Format:</b> Excel CSV</p>
  
  
  <p>The <b>objectives</b> of this repository was to practice beginner techniques of python by iterating through CSV data to return results that meet conditions, sumate the values per categorical data & structure the final result into a legible format for reporting.</p>
  <p> Also, demonstrated was a technique called List Comprehension, which was efficent short hand that still displayed readable logic to the developer.</p>
  <p> Lastly, the result of these excerises were to print the results in the console & to export the result into .txt file format.</p>
</div>

<h2> Code Samples 📓</h2>
<p> Sample from: Python_For_and_While_Loops</p>

```python
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
 ```

