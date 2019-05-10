#Read a csv file 
#set variables to the data
#write a new .txt file 
#write headers and rows 
#write code

import os
import csv
# to refer to csv file
pybank_data= os.path.join('.','homework_03-Python_Instructions_PyBank_Resources_budget_data (1).csv')

# to open csv file
with open(pybank_data,'r', newline='') as pybankfile:
    pyBdata_reader= csv.DictReader(pybankfile, delimiter=',')
    
    #to print the number of months :3
    list_sum=0
    for lines in pyBdata_reader:
        list_sum = list_sum + (len(lines))/2 
    print("Financial Analysis")
    print("--------------------------------")
    print(f'Total Months: {list_sum}')  
                
          
          
           
        
    #source[mergedict]:https://stackoverflow.com/questions/5946236/how-to-merge-multiple-dicts-with-same-key
    #source[csvread&write]: https://www.youtube.com/watch?v=q5uM4VKywbA&t=266s ** helped the most
    #source[csv&python]:https://www.programiz.com/python-programming/working-csv-files 
    #source[readlines]:https://docs.python.org/2/tutorial/inputoutput.html
    #source[to identify columns]:https://stackoverflow.com/questions/16503560/read-specific-columns-from-a-csv-file-with-csv-module 