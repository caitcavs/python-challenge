# import, read, and open csv file
import csv
import os

budget_csv = os.path.join('budget_data.csv')

with open(budget_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # skip header
    csv_header = next(csv_reader)
    # set variables to start
    total_months = []
    total_pl = []
    pl_changes = []
    
    # start for loop  
    for row in csv_reader:
        # all months in dataset to total months list, allowing us to find length of list for total months
        total_months.append(row[0])  
        # all Profits/Losses to net total list, allowing us to add all values and fine net total
        total_pl.append(int(row[1])) 
    

    #finding the average of the changes over the given period using a variable
    for x in range(1, len(total_pl)):
        #adding values for difference in profits/losses by subtracting next cell from previous cell
        pl_changes.append(int(total_pl[x])-int(total_pl[x-1]))
   
    #finding the sum of P/L changes within its list and dividing by the total number of months
    average_pl = sum(pl_changes)/(len(total_months)-1)


 
    

# finding values for min and max within the Profits/Losses changes list
greatest_increase = max(pl_changes)
greatest_decrease = min(pl_changes)

#Find corresponding month/year for min/max values

months = len(total_months)

# export text file
with open('financialanalysis.txt', 'w') as txt_file:
    output = 'Financial Analysis\n----------------------------------\n' 
    print(output)
    txt_file.write(output)
    txt_file.write('Total Months:' + str(months) + "\n")
    txt_file.write('Net Total: ' + str(sum(total_pl)) + "\n")
    txt_file.write('Average Change: ' + str(average_pl) + "\n")
    txt_file.write('Greatest Increase in Profits: ' + str(greatest_increase) + "\n")
    txt_file.write('Greatest Decrease in Profits: ' + str(greatest_decrease))


    # total number of months
    print('Total Months:', len(total_months))
    # net total of Profits/Losses
    print('Net Total:', '$', sum(total_pl))
    # Average P/L Change
    print('Average Change:', '$', int(average_pl))
    # The greatest increase in profits with date and amount
    print('Greatest Increase in Profits:', greatest_increase)
    # The greatest decrease in profits with date and amount
    print('Greatest Decrease in Profits:', greatest_decrease)


