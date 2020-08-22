# @TODO: Your code here
import os
import csv

csvpath = os.path.join(".","Resources","budget_data.csv")


month_counter = 0
net_total = 0

with open(csvpath) as csvfile:
    
    readCSV = csv.reader(csvfile,delimiter = ',')
    headers = next(readCSV)
    
    max_money = 0
    min_money = 0
    for row in readCSV:
        if month_counter == 0:
            max_money = int(row[1])
            min_money = int(row[1])
        print(row)
        date = row[0]
        money = int(row[1])
        month_counter+=1
        net_total += money
        if money>max_money:
            max_money = money
        if money<min_money:
            min_money = money
        print(date)
        print(money)
        print(net_total)
        print(max_money)
        print(min_money)


output_file = os.path.join(".","analysis", "output.txt") 
      
f=open(output_file, "a")
print("Financial Analysis \n----------------------\nTotal Months: " + str(month_counter), file=f)
    
print(" \nTotal:" + str((net_total)), file=f)
print(" \nAverage Change: " + str(net_total/month_counter), file=f)
print("\nGreatest Increase in Profits: " + str(max_money), file=f)
print("\nGreatest Decrease in Profits: "+ str(min_money), file=f)
f.close()
        
