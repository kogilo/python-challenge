# import the csv and os modules in order to read the data in to computer
import csv
import os
# Copy the path for budget_data_1.csv or budget_data_2.csv  into os.path.join("") as below

budget_data = os.path.join("/Users/abulla/Desktop/python/pybank/budget_data_1.csv")
# initially create an empty row the hold the variables 'Date' & 'Revenue'.
# Note that they are columns 
Dates = []
Revenue = []

# Read in the file with csv.reader()and store it in an object called 'budget_data_list'.
with open(budget_data, 'r') as csvfile:
    ## Create a list by looping through each line in csvfile
    budget_data_list = csv.reader(csvfile)
    
    next(budget_data_list, None)
    # append the 'Dates' & 'Revenue' to 'budget_data_list'.
    for row in budget_data_list:
        Dates.append(row[0])
        Revenue.append(int(row[1]))

#count the total_months
total_months = len(Dates)

#create a list for revenue change
greatest_increase = Revenue[0]
greatest_decrease = Revenue[0]
total_revenue = 0

#loop through revenue list to find the change in revenue from month.
for i in range(len(Revenue)):
    if Revenue[i] >= greatest_increase:
        greatest_increase = Revenue[i]
        great_inc_month = Dates[i]
    elif Revenue[i] <= greatest_decrease:
        greatest_decrease = Revenue[i]
        great_dec_month = Dates[i]
    total_revenue += Revenue[i]

#Find the average_change and round it to two decimal place.
average_change = round(total_revenue/total_months, 2)

#Sets path for budget_summary and use the writelines() function to write the summary
budget_summary = os.path.join("/Users/abulla/Desktop/python/pybank/budget_data_1.csv")
with open(budget_summary, 'w') as budgetsummary:
    budgetsummary.writelines('Financial Analysis\n')   # use '\n' to break the line
    budgetsummary.writelines('=======================' + '\n')
    budgetsummary.writelines('Total Months: ' + str(total_months) + '\n')
    budgetsummary.writelines('Total Revenue: $' + str(total_revenue) + '\n')
    budgetsummary.writelines('Average Revenue Change: $' + str(average_change) + '\n')
    budgetsummary.writelines('Greatest Increase in Revenue: ' + great_inc_month + ' ($' + str(greatest_increase) + ')'+ '\n')
    budgetsummary.writelines('Greatest Decrease in Revenue: ' + great_dec_month + ' ($' + str(greatest_decrease) + ')')

#Finally Read the summary by including 'r' 
with open(budget_summary, 'r') as readfile:
    print(readfile.read())

