import os
import csv
import sys

csv_path = os.path.join(".", "election_data_1.csv")

with open(csv_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    num_votes = []
    candidates = []
    who_ran = []
    final_percent = []
    ind_votes = []
    for row in csvreader:
        num_votes.append(row[2])
        candidates.append(row[2])
    for c in candidates:
        if c not in who_ran:
            who_ran.append(c)
    for x in who_ran:
        ind_votes.append(candidates.count(x))
    total_votes = len(num_votes)
    high_votes = max(ind_votes)
    for p in ind_votes:
        final_percent.append((p / total_votes) * 100)
        if p == high_votes:
            winner_index = ind_votes.index(p)
    winner = who_ran[winner_index]

print("Election Results")
print("------------------")
print("Total Votes: " + str(total_votes))
print("------------------")
print(who_ran[0] + ": " + str(final_percent[0]) + "%  " + str(ind_votes[0]))
print(who_ran[1] + ": " + str(final_percent[1]) + "%  " + str(ind_votes[1]))
print(who_ran[2] + ": " + str(final_percent[2]) + "%  " + str(ind_votes[2]))
print(who_ran[3] + ": " + str(final_percent[3]) + "%  " + str(ind_votes[3]))
print("------------------")
print("Winner: " + str(winner))
print("------------------")