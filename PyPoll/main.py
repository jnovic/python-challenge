# PyPoll Challenge
import os
import csv

csvpath = os.path.join(r"C:/Users/jnovic/Desktop/CWUBootcamp/PyPoll/Resources/election_data.csv")

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    count = 0
    for row in csvreader:
        count += 1
    print(count)