import os
import csv

csvpath=os.path.join("Resources","election_data.csv")
print(csvpath)
#tracks the total votes cast
total_vote_cast=0
candidate_info={}



#opening the csv file
with open(csvpath,'r') as voter_data:
    #reading from csv
    vote_reader=csv.reader(voter_data)

    # reading the Header
    voter_header = next(vote_reader)
    print(f"CSV Header: {voter_header}")

    for row in vote_reader:
        #calculating the the total months in dataset
        total_vote_cast+=1
        if row[2] in candidate_info:
            candidate_info[row[2]]=candidate_info[row[2]]+1
        else:
            candidate_info[row[2]]=1
    
print("Election Results")
print("--------------------------------------")
print(f'Total Votes : {total_vote_cast}')
print("-----------------------------------------")
winner_candidate_name=''
winner_candidate_votes=0
for name,votes in candidate_info.items():
    print(f'{name} : {round(votes/total_vote_cast*100,3)}% ({votes}) ')
    if (votes>winner_candidate_votes):
        winner_candidate_name=name
        winner_candidate_votes=votes
print("----------------------------------------")
print(f"Winner : {winner_candidate_name}")
print("----------------------------------------")

output_file = os.path.join("Resources","Election Results.txt")

 #Open the output file
with open(output_file, "w", newline="") as textfile:
    textfile.write("Election Results\n")
    textfile.write("-----------------------------------------\n")
    textfile.write(f'Total Votes : {total_vote_cast}\n')
    textfile.write("-----------------------------------------\n")
    for name,votes in candidate_info.items():
        textfile.write(f'{name} : {round(votes/total_vote_cast*100,3)} % ({votes})\n ')
    textfile.write("-----------------------------------------\n")
    textfile.write(f"Winner : {winner_candidate_name}\n")
    textfile.write("-----------------------------------------\n")


