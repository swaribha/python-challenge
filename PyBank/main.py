import os
import csv

csvpath=os.path.join("Resources","budget_data.csv")
print(csvpath)
#tracks the total months in sheet
total_months=0
#for net profit or losses 
total_pl=0
#for capturing gratest increase
max_increase={"Date":0,"Amount":0}
#for maximum decrease in losses
max_decrease={"Date":0,"Amount":0}
#avgerage change_month in profit
previous_pl=0
PL_change=[]
avg_change=0

#opening the csv file
with open(csvpath,'r') as budgetdata:
    #reading from csv
    budget_reader=csv.reader(budgetdata)

    # reading the Header
    budget_header = next(budget_reader)
    print(f"CSV Header: {budget_header}")

    for row in budget_reader:
        #calculating the the total months in dataset
        total_months+=1
        #Net profit/losses over the entire period
        total_pl+=int(row[1])
        change_month = int(row[1])-previous_pl
        PL_change.append(change_month)
        previous_pl=int(row[1])
        #finding if change is greater then previous increase
        if change_month > max_increase["Amount"]:
            max_increase["Amount"]=change_month
            max_increase["Date"]=row[0]
        #if change is smaller then previous decrase
        if change_month <max_decrease["Amount"]:
            max_decrease["Amount"]=change_month
            max_decrease["Date"]=row[0]

#calculating the average change
#removing the first element of list 
PL_change.pop(0)
total_change=sum(PL_change)
avg_change=round(total_change/len(PL_change),2)

#printing output to Terminal
print(f'Financial Analysis')
print('-------------------------------------------------------')
print(f'Total months : {total_months}')
print(f'Total : ${total_pl}')
print(f'Average  Change: ${avg_change}')
print(f'Greatest Increase in profit : {max_increase["Date"]} (${max_increase["Amount"]})')
print(f'Greatest Decrease in profit : {max_decrease["Date"]} (${max_decrease["Amount"]})')


output_file = os.path.join("Resources","Financial Analysis.txt")

#  Open the output file
with open(output_file, "w", newline="") as textfile:
    textfile.write(f'Financial Analysis\n')
    textfile.write('-------------------------------------------------------\n')
    textfile.write(f'Total months : {total_months}\n')
    textfile.write(f'Total : {total_pl}\n')
    textfile.write(f'Average  Change: {avg_change}\n')
    textfile.write(f'Greatest Increase in profit : {max_increase["Date"]} (${max_increase["Amount"]})\n')
    textfile.write(f'Greatest Decrease in profit : {max_decrease["Date"]} (${max_decrease["Amount"]})\n')

    
