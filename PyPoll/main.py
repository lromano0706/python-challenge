# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "PyPoll_Resources_election_data.csv")

# Track various financial parameters
total_months = 0
Total_Count = 0
Khan_Count = []
Khan_Total = 0
Correy_Count = []
Correy_Total = 0
Li_Count = []
Li_Total = 0
OTooley_Count = []
OTooley_Total = 0
X = []
Khan_win_percent = 0



# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as Vote_Data:
	reader = csv.reader(Vote_Data)
# Read the header row
	header = next(reader)
	VoterList = list(reader)
#Total Count
Total_Count = len(VoterList)
Total_Count = int(Total_Count)

#Count for Khan, Correy, Li and O'Tooley
for X in VoterList:
	if X[2] == 'Khan':
		Khan_Count.append(X[0])
		Khan_Total = len(Khan_Count)
	elif X[2] == 'Correy':
		Correy_Count.append(X[0])
		Correy_Total = len(Correy_Count)
	elif X[2] == 'Li':
		Li_Count.append(X[0])
		Li_Total = len(Li_Count)
	elif X[2] == 'O\'Tooley':
		OTooley_Count.append(X[0])
		OTooley_Total = len(OTooley_Count)


# win percentage for Khan, Correy, Li and O'Tooley
Khan_win_percent = (Khan_Total / Total_Count) * 100
Correy_win_percent = (Correy_Total / Total_Count) * 100
Li_win_percent = (Li_Total / Total_Count) * 100
OTooley_win_percent = (OTooley_Total / Total_Count) * 100

#Results list
Results = {Khan_win_percent: 'Khan', Correy_win_percent: 'Correy', Li_win_percent: 'Li', OTooley_win_percent: 'O\'Tooley'}
Winner = max(Results)
Winner_Name = (Results[Winner])


# Print on to the screen
print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes:  {Total_Count}')
print(f'Khan: {Khan_win_percent:.3f}% ({Khan_Total}) ')
print(f'Correy: {Correy_win_percent:.3f}% ({Correy_Total})')
print(f'Li: {Li_win_percent:.3f}% ({Li_Total})')
print(f'O\'Tooley: {OTooley_win_percent:.3f}% ({OTooley_Total})')
print(f'-------------------------')
print(f'Winner: {Winner_Name}  ')
print(f'-------------------------')


		# Specify the file to write to
output_path = os.path.join('analysis', 'VoteResults.txt')

with open(output_path, 'w', newline='') as txtfile:

	    # Initialize csv.writer
    csvwriter = csv.writer(txtfile, delimiter=',')

        # Write the first row (column headers)
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-------------------------'])

        # Write in Analysis Text File
    csvwriter.writerow([f'Total Votes: {Total_Count} '])
    csvwriter.writerow([f'-------------------------'])
    csvwriter.writerow([f'Total Votes:  {Total_Count}'])
    csvwriter.writerow([f'Khan: {Khan_win_percent:.3f}% ({Khan_Total})'])
    csvwriter.writerow([f'Correy: {Correy_win_percent:.3f}% ({Correy_Total})'])
    csvwriter.writerow([f'Li: {Li_win_percent:.3f}% ({Li_Total})'])
    csvwriter.writerow([f'O\'Tooley: {OTooley_win_percent:.3f}% ({OTooley_Total})'])
    csvwriter.writerow([f'-------------------------'])
    csvwriter.writerow([f'Winner: {Winner_Name}  '])
    csvwriter.writerow([f'-------------------------'])

