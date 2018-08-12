# PyBank Challenge
import os
import csv

csvpath = os.path.join(r"C:/Users/jnovic/Desktop/CWUBootcamp/PyBank/Resources/budget_data.csv")

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader, None)
    
    list_changes = []
    count = 0
    profit = 0.00  
    for row in csvreader:
        count += 1
        profit += float(row [1])
            
    
    print(count)
    print(profit)
 
    
    
    
    
