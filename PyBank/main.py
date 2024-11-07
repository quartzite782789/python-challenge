# -*- coding: UTF-8 -*-
"""PyBank Homework CThomas Solution"""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
start=[]    #List of the first entry
profloss=[] #List to store Profit/Loss entries
net_change_list=[]  #List to store calculated net changes
i=0     #Index counter for profloss[i] and net_change_list[i-1]
gi=0    #Greatest increase value
gim=0   #Greatest increase month
gd=0    #Greatest decrease value
gdm=0   #Greatest decrease month
avg=0   #Average net change

# Print Variables
output="N/A"    #String variable to store the print/write output of the results summary

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    start=next(reader)
    total_months=total_months+1 #Count first line date
    profloss=[int(start[1])]    #Start profloss with first entry

    # Process each row of data
    for row in reader:
        total_months=total_months+1 #Increase Month count
        profloss.append(int(row[1]))    #Append the current Profit/Loss entry to profloss

        # Track the total
        total_net=sum(profloss)

        # Track the net change
        i=i+1   #Advance the index
        net_change_list.append(profloss[i]-profloss[i-1])
        
        # Calculate the greatest increase in profits (month and amount)
        if (net_change_list[i-1])>gi:   #If higher net change encountered, record it and the month
            gi=net_change_list[i-1]
            gim=row[0]

        # Calculate the greatest decrease in losses (month and amount)
        elif (net_change_list[i-1])<gd: #If lower net change encountered, record it and the month
            gd=net_change_list[i-1]
            gdm=row[0]
        
# Calculate the average net change across the months
avg=round(sum(net_change_list)/len(net_change_list),2)

# Generate the output summary by appending together string variable "output"
output=f"Financial Analysis\n----------------------------\nTotal Months: {total_months}\n"
output+=f"Total: ${total_net}\nAverage Change: ${avg}\n"
output+=f"Greatest Increase in Profits: {gim} (${gi})\nGreatest Decrease in Profits: {gdm} (${gd})\n"

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
