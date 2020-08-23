# @TODO: Your code here
import os
import csv

csvpath = os.path.join(".","Resources","budget_data.csv")


month_counter = 0
net_total = 0
month_prior = 0
total_change = 0
with open(csvpath) as csvfile:
    
    readCSV = csv.reader(csvfile,delimiter = ',')
    headers = next(readCSV)
    
    max_change = 0
    max_date = ""
    min_change = 0
    min_date = ""
    for row in readCSV:
        
       
        date = row[0]
        money = int(row[1])
        
        net_total += money
        current_change = money - month_prior
        if month_counter != 0:
            total_change += current_change
        if month_counter == 0:
            max_change = current_change
            max_date = date
            min_change = current_change
            min_date = date
        if current_change > max_change:
            max_change = current_change
            max_date = date
        if current_change < min_change:
            min_change = current_change
            min_date = date
        month_prior = money
        month_counter+=1
        """
        print("----------------")
        print(date)
        print("this date's addition: " + str(money))
        print("this date's change: " + str(current_change))

        print("total change: " + str(total_change))
        print("max change: " + str(max_change))
        print("min change: " + str(min_change))
        print(month_counter)
        """
    average_change = total_change/(month_counter-1)
    #print the next five lines into .txt

    print("Financial Analysis \n----------------------\nTotal Months: " + str(month_counter))
    print("Total: $" + str(net_total))
    print("Average Change: $%.2f" %average_change)
    print("Greatest Increase in Profits: " + max_date + " ($" + str(max_change) + ")")
    print("Greatest Decrease in Profits: " + min_date+ " ($" +  str(min_change) + ")")


output_file = os.path.join(".","analysis", "output.txt")  
f=open(output_file, "a")  
print("Financial Analysis \n----------------------\nTotal Months: " + str(month_counter), file=f)
print("Total: $" + str(net_total), file=f)
print("Average Change: $%.2f" %average_change, file=f)
print("Greatest Increase in Profits: " + max_date + " ($" + str(max_change) + ")", file=f)
print("Greatest Decrease in Profits: " + min_date+ " ($" +  str(min_change) + ")", file=f)
f.close()    

