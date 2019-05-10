import os
import csv


# to refer to csv file
pybank_data= os.path.join('.','homework_03-Python_Instructions_PyBank_Resources_budget_data (1).csv')

def TotalsBankData(pyBankData):
    months = str(pyBankData[0])
    profits = int(pyBankData[1])

    print(f"Total Months:{months}")
    print(f"Total: {profits}")
# to open csv file
with open(pybank_data,'r', newline='') as pybankfile:
    pyBdata_reader= csv.reader(pybankfile, delimiter=',')

#------------------------------to format data to print---------------------------------
    #variables will be used to create list of date and profit columns
    months=[]
    profit=[]
    
    for lines in pyBdata_reader:
        # to create a list of the date column
        columns=list(lines)
        datecol= columns[0]
        months.append(datecol)
        # to create a list of the profit column
        profit_col= columns[1]
        profit.append(profit_col)
    months.pop(0)
    profit.pop(0)
    #-----------------set finale variables to print--------------------------------------
    #to calculate total # of months (-1 is to remove header)
    tot_months=len(months)
    #to make profit strings into values 
    profitvalue= [int(x) for x in profit[0:]]
    #to calculate sum of profit&loss
    tot_prof =sum(profitvalue)
    #to calculate average of profit&loss
    average= int(tot_prof/len(profitvalue))
    #to calculate avg diff in profit&loss
    diff_value= [profitvalue[i+1]-profitvalue[i] for i in range(len(profitvalue)-1)]
    average_diffv= round(sum(diff_value)/len(diff_value),2)
    #to calculate the max diff in profit&loss
    max_diffv= max(diff_value)
    #to get the index of the max value
    month_ref= [i for i, j in enumerate(diff_value) if j == max_diffv]
    month_refv= int(month_ref[0])
    #to get the month per month_ref from months list
    max_month= [j for i, j in enumerate(months) if i == (month_refv+1)]
    
    
#------------------------------print-----------------------------------------------------    
    print("Financial Analysis")
    print("--------------------------")
    print(f"Total Months: {tot_months}")
    print(f"Total: ${tot_prof}")
    print(f"*Average Value: ${average}")
    print(f"Average Change: $ {average_diffv}")
    print(f"Greatest Increase in Profits: {max_month[0]} (${max_diffv})")
    
    
    #print(f"Greatest Increase in Profits:)
    
          
    #source[enumeratealistforref]:https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-given-a-list-containing-it-in-python      
    #source[iterate&getlistofdiff]:https://stackoverflow.com/questions/2400840/finding-differences-between-elements-of-a-list     
    #source[covertlistofstrtoint]:https://stackoverflow.com/questions/21493924/is-there-a-way-to-loop-through-a-list-and-convert-everything-to-integers    
    #source[mergedict]:https://stackoverflow.com/questions/5946236/how-to-merge-multiple-dicts-with-same-key
    #source[csvread&write]: https://www.youtube.com/watch?v=q5uM4VKywbA&t=266s ** helped the most
    #source[csv&python]:https://www.programiz.com/python-programming/working-csv-files 
    #source[readlines]:https://docs.python.org/2/tutorial/inputoutput.html
    #source[to identify columns]:https://stackoverflow.com/questions/16503560/read-specific-columns-from-a-csv-file-with-csv-module 