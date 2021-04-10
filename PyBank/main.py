
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

# Set path for file
MyBank = os.path.join('Resources','budget_data.csv')

# Lists to store data
Data_Set = []
Total_Prof_Loss = []
Date = []
Total = 0 
Change = []

# Open the CSV
with open(MyBank) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
#Header info not needed
	csv_header = next(csvreader, None)
#Find Total Months
	Data_Set = list(csvreader)
	Total_Months = len(Data_Set)
#For loop to find total
	for i in Data_Set:
		Total_Prof_Loss.append(int(i[1]))
		Date.append(i[0])

	Total = sum(Total_Prof_Loss)

#For loop to append average list and to get min and max
	for j in range(1,len(Total_Prof_Loss)):
		Change.append(Total_Prof_Loss[j] - Total_Prof_Loss[j-1])
		Greatest_increase = max(Change)
		Greatest_decrease = min(Change)
	
	Average = sum(Change) / len(Change)

	Greatest_Date = str(Date[Change.index(max(Change)) + 1])
	Lowest_Date = str(Date[Change.index(min(Change)) + 1])

#print on to screen
print(f'Financial Analysis')
print(f'----------------------------')
print(f'Total Months: {Total_Months}')
print(f'Total: ${Total:,}')
print(f'Average Change: ${Average:.2f}')
print(f'Greatest Increase in Profits: {Greatest_Date} (${Greatest_increase:,})')
print(f'Greatest Decrease in Profits: {Lowest_Date} (${Greatest_decrease:,})')

		# Specify the file to write to
output_path = os.path.join('analysis', 'PyBankResults.txt')

with open(output_path, 'w', newline='') as txtfile:

	    # Initialize csv.writer
    csvwriter = csv.writer(txtfile, delimiter=',')

        # Write the first row (column headers)
    csvwriter.writerow([f'Financial Analysis'])
    csvwriter.writerow([f'----------------------------'])

        # Write in Analysis Text File
    csvwriter.writerow([f'Total Months: {Total_Months}'])
    csvwriter.writerow([f'Total: ${Total}'])
    csvwriter.writerow([f'Average Change: ${Average:.2f}'])
    csvwriter.writerow([f'Greatest Increase in Profits: {Greatest_Date} (${Greatest_increase})'])
    csvwriter.writerow([f'Greatest Decrease in Profits: {Lowest_Date} (${Greatest_decrease})'])





