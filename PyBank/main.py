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
    pyBdata_reader= csv.DictReader(pybankfile)

    
    for line in pyBdata_reader:
       num_months= line['Date'] 
        #print(num_months)

    #source[csvread&write]: https://www.youtube.com/watch?v=q5uM4VKywbA&t=266s ** helped the most
    #source[csv&python]:https://www.programiz.com/python-programming/working-csv-files 
    #source[readlines]:https://docs.python.org/2/tutorial/inputoutput.html
    #source[to identify columns]:https://stackoverflow.com/questions/16503560/read-specific-columns-from-a-csv-file-with-csv-module 
  