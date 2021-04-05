# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

# Set path for file
MyBank = os.path.join('Pybank','Resources','budget_data.csv')

# Lists to store data
Date = []
Total = []
Total_Prof_Loss = []
Change_Prof_Loss = []
Great_Increase =[]
Great_Decreas = []

# Open the CSV
with open(MyBank) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
# Defining values and storing data deleted first row

	averagelist = list(csvreader)
	del averagelist[0]
	Total_Months = 0
	First_Month_Value = averagelist[0]
	Last_Month_Value = averagelist[-1]
	First_Month_Amount = First_Month_Value[1]
	Last_Month_Amount = Last_Month_Value[1]

	

#Header info not needed
	
	csv_header = next(csvreader, None)

#Read the rows in the csv file
	for row in averagelist:

#Add Total Profit/loss values
		Total.append(int(row[1]))
		Total_Prof_Loss = sum(Total) 
#Find Greatest Increase
	

#Total months
Total_Months = len(averagelist)
Total_Months = int(Total_Months)

#Average change
Change_Prof_Loss = (int(First_Month_Amount) - int(Last_Month_Amount)) / (Total_Months - 1)




	

print(f"Total Months: {Total_Months}")
print(f"Total: ${Total_Prof_Loss}")
print(f"Average Change: {Change_Prof_Loss}")
print(f"Greatest Increase in Profits: ")
print(f"Greatest Decrease in Profits: ")

		# Specify the file to write to
output_path = os.path.join('Pybank', 'analysis', 'new.txt')

with open(output_path, 'w', newline='') as txtfile:

	    # Initialize csv.writer
    csvwriter = csv.writer(txtfile, delimiter=',')

        # Write the first row (column headers)
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['------------------'])

        # Write in Analysis Text File
    csvwriter.writerow(['Total Months: %s' % Total_Months])
    csvwriter.writerow(['Total: $%s' % Total_Prof_Loss ])
    csvwriter.writerow(['Average Change: %s' % Change_Prof_Loss])
    csvwriter.writerow(['Greatest Increase of Profits: '])
    csvwriter.writerow(['Greatest Decrease of Profits: '])




