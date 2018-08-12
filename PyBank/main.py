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
    calc_change = 0
    calc_average = 0
    #max_month = [csvreader[24]]
    #min_month = [csvreader[44]]
    
    for row in csvreader:
        count += 1
        profit += float(row [1])
        list_changes.append(int(row[1]) - calc_change) 
        test = int(row [1])
        
    for item in list_changes:
        calc_average += item
    
    average = round(calc_average/count, 2) 
    maximum = max(list_changes) 
    minimum = min(list_changes)
      
    print(count)
    print(profit)
    print(maximum)
    print(minimum)
    print(average)
    
    print("Financial Analysis")
    print("------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total: $" + str(profit))
    print("Average Change: $" + str(average))
    print("Greatest Increase in Profits: $" + str(maximum))
    print("Greatest Increase in Profits: $" + str(minimum))
    
