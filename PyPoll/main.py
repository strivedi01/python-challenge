import os
import csv
import itertools



csvpath = os.path.join(".","Resources","election_data.csv")
print(csvpath)
with open(csvpath) as csvfile:
    vote_count = 0
    khan_count = 0
    correy_count = 0
    li_count = 0
    tooley_count = 0

    readCSV = csv.reader(csvfile,delimiter=',')
    headers = next(readCSV)
    for row in readCSV:
        
        voterID = row[0]
        county = row[1]
        vote = row[2]
        vote_count += 1
        print(vote_count)
        if vote == 'Khan':
            khan_count += 1
        elif vote =='Correy':
            correy_count += 1 
        elif vote == "O'Tooley":
            tooley_count += 1
        else:
            li_count += 1
        
output_file = os.path.join(".","analysis", "poll_output.txt")  
f=open(output_file, "a")
print("Election Results \n -----------------\n Total Votes: " + str(vote_count) + "\n-----------------", file=f)
    
print("Khan: %.3f"%((khan_count/vote_count)*100) + "%" + "(%.0f)"% khan_count, file=f)
print("Correy: %.3f"%((correy_count/vote_count)*100) + "%" + "(%.0f)"% correy_count, file=f)
print("Li: %.3f"%((li_count/vote_count)*100) + "%" + "(%.0f)"% li_count, file=f)
print("O'Tooley: %.3f"%((tooley_count/vote_count)*100) + "%" + "(%.0f)"% tooley_count, file=f)

d = {'Khan': khan_count, 'li': li_count, 'correy': correy_count,"O'Tooley": tooley_count}
v= list(d.values())
k= list(d.keys())
print("Winner: " +  k[v.index(max(v))], file=f)
f.close()





    


