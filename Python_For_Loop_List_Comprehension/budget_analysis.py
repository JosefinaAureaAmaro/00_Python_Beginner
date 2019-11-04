# dependancies
import os
import csv

# to refer to csv file
data = os.path.join('.','budget_data.csv')

# to open csv file
with open(data,'r', newline='') as budget_file:
    budget_data_reader = csv.reader(budget_file, delimiter=',')

#------------------------------ store data into variables from csv ---------------------------------

    # variables will be used to create list of date and profit columns
    months = []
    profit = []
    
    for rows in budget_data_reader:
        # to create a list of the date column
        columns = list(rows)

        ##  to gather data by column 

        # date
        date_col = columns[0]
        months.append(date_col)


        # profit values
        profit_col= columns[1]
        profit.append(profit_col)

    # to remove headers from data
    months.pop(0)
    profit.pop(0)


    #----------------- Budget Analysis --------------------------------------


    # Calculate total number of months reviewed
    tot_months = len(months)

    ## Profit & Loss Value Review ##

    # Reformat Data: convert profit value strings to intergers
    profit_values = [int(x) for x in profit]

    # to calculate sum of profit&loss
    tot_prof = sum(profit_values)

    # to calculate average of profit&loss
    average_profit = round((tot_prof/ tot_months), 0)

    # to make list of values for list comprehension 

    # to calculate avg variance in profit&loss month over month
    profit_variance = [profit_values[i+1] - profit_values[i] for i in range((tot_months -1))]

    # to calcualte average profit variance
    average_profit_variance = round( sum(profit_variance)/len(profit_variance) ,2)

    # to calculate the largest variance in profit&loss
    max_profit_variance = max(profit_variance)

    # to get the index of the max value
    index_of_max_profit_variance = profit_variance.index(max_profit_variance)

    # to get the month of max profit variance
    month_of_max_profit_variance = months[index_of_max_profit_variance]

    # to calculate the lowest variance in profit&loss
    min_profit_variance = min(profit_variance)

    # to get the index of the max value
    index_of_min_profit_variance = profit_variance.index(min_profit_variance)

    # to get the month of the lowest profit variance
    month_of_min_profit_variance = months[index_of_min_profit_variance]
    
    budget_analysis_results = (f"""Financial Analysis\n
                    --------------------------\n
                    Total Months: {tot_months}\n
                    Total: ${tot_prof}\n
                    Average Profit Value: ${average_profit}\n
                    Average Profit Variance: $ {average_profit_variance}\n
                    Largest Increase in Profitability: {month_of_max_profit_variance} (${max_profit_variance})\n
                    Largest Descrease in Profitability: {month_of_min_profit_variance} (${min_profit_variance})""")

    
print(budget_analysis_results)
    
    
 
    #-------------to print budget analysis to a .txt file-------

import sys

budget_data_path = os.path.join('.','budget_analysis_results.txt')
with open(budget_data_path,'w') as budget_analysis_file:
    sys.stdout = budget_analysis_file

    print(budget_analysis_results)
