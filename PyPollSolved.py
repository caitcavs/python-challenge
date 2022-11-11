import csv
import os


candidates = {}
#define initial variables
total_votes = 0
election_winner_count = 0
election_winner = ''
#path
poll_csv = os.path.join('election_data.csv')
#open and read csv file
with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    #create a loop through whole csv file
    for row in csvreader:
        #set a variable to the candidates column
        candidate_name = row[2]
        #as loop continues, add 1 to total votes
        total_votes = total_votes + 1

        if candidate_name in candidates:
            candidates[candidate_name] = candidates[candidate_name] + 1
        else:
            candidates[candidate_name] = 1
# determine the election winner by looping through all candidates and getting most vote count
for candidate_name, candidate_votes in candidates.items(): 
    if candidate_votes > election_winner_count:
        election_winner = candidate_name


# set variables
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]

# Calculate vote percentages
percent_candidate1 = len(candidates[0])/total_votes
percent_candidate2 = len(candidates[1])/total_votes
percent_candidate3 = len(candidates[2])/total_votes



#total_candidate1 = 
# print statements
print("Total Votes: ", total_votes)
print('\n -------------------------')
print(candidates[0], (percent_candidate1))
print(candidates[1], percent_candidate2)
print(candidates[2], percent_candidate3)
print('\n -------------------------')
print('Winner: ', election_winner)

# create txt file and write results to it
with open('election_results.txt', 'w') as txt_file:
    output = 'Election Results\n----------------------------------\n'
    print(output)
    txt_file.write(output)
    txt_file.write(str(candidates[0]) + str(percent_candidate1) + '\n')
    txt_file.write(str(candidates[1]) + str(percent_candidate2) + '\n')
    txt_file.write(str(candidates[2]) + str(percent_candidate3) + '\n')
    txt_file.write('Winner: ' + str(election_winner))
