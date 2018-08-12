# PyPoll Challenge
import os
import csv

csvpath = os.path.join(r"C:/Users/jnovic/Desktop/CWUBootcamp/PyPoll/Resources/election_data.csv")

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader, None)
    vote_count = [0, 0, 0, 0]
    candidates = ["Khan", "Correy", "Li", "O'Tooley"]
    
    count = 0
    for row in csvreader:
        count += 1
        if row[2] == "Khan":
            vote_count[0] += 1
        if row[2] == "Correy":
            vote_count[1] += 1
        if row[2] == "Li":
            vote_count[2] += 1
        if row[2] == "O'Tooley":
            vote_count[3] += 1
    
    vpercent = [round(x/count*100, 2) for x in vote_count]
     
    print("Election Results")
    print("--------------------------------------------")
    print("Total Votes: " + str(count))
    print("--------------------------------------------")
    print(candidates[0] + " " + str( vpercent[0]) + " (" + str(vote_count[0]) + ")")
    print(candidates[1] + " " + str( vpercent[1]) + " (" + str(vote_count[1]) + ")")
    print(candidates[2] + " " + str( vpercent[2]) + " (" + str(vote_count[2]) + ")")
    print(candidates[3] + " " + str( vpercent[3]) + " (" + str(vote_count[3]) + ")")
    print("---------------------------------------------")
    print("Winner = Khan")
    
    file = open("C:/Users/jnovic/Desktop/python-challenge/PyPoll/Pypol.txt", "w")
    file.write("Election Results")
    file.write("--------------------------------------------")
    file.write("Total Votes: " + str(count))
    file.write("--------------------------------------------")
    file.write(candidates[0] + " " + str( vpercent[0]) + " (" + str(vote_count[0]) + ")")
    file.write(candidates[1] + " " + str( vpercent[1]) + " (" + str(vote_count[1]) + ")")
    file.write(candidates[2] + " " + str( vpercent[2]) + " (" + str(vote_count[2]) + ")")
    file.write(candidates[3] + " " + str( vpercent[3]) + " (" + str(vote_count[3]) + ")")
    file.write("---------------------------------------------")
    file.write("Winner = Khan")
    
    file.close()
    
    