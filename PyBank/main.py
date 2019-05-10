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
    
    months=[]
    profit=[]
    
    for lines in pyBdata_reader:
        columns=list(lines)
        datecol= columns[0]
        months.append(datecol)
        profit_col= columns[1]
        profit.append(profit_col)
    print(months)
    print(profit)
    
    #profit=[]
    
   # for lines_p in pyBdata_reader:
       # columns_p= list(lines_p)
       # print(columns_p)
        #datecol_p= columns_p[1]
        #profit.append(datecol_p)
    #print(profit)
       
        
   # print(lines)
        
        #Concat_list_col= Datecol + lines
        #print(concat_list_col)
        #for items in columns:
            #print(items)
        
    
    #header= next(pyBdata_reader)
    
    #to print the number of months :3
    #list_sum=0
    #for lines in pyBdata_reader:
       # print(lines,)
        #TotalsBankData(lines)
        
        
        #list_sum = list_sum + (len(lines))/2 
    #print("Financial Analysis")
    #print("--------------------------------")
   # print(f'Total Months: {list_sum}')  
                
          
          
           
        
    #source[mergedict]:https://stackoverflow.com/questions/5946236/how-to-merge-multiple-dicts-with-same-key
    #source[csvread&write]: https://www.youtube.com/watch?v=q5uM4VKywbA&t=266s ** helped the most
    #source[csv&python]:https://www.programiz.com/python-programming/working-csv-files 
    #source[readlines]:https://docs.python.org/2/tutorial/inputoutput.html
    #source[to identify columns]:https://stackoverflow.com/questions/16503560/read-specific-columns-from-a-csv-file-with-csv-module