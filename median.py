import csv
with open("SOCR-HeightWeight.csv" , newline = "" ) as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
newData = []
for i in range(len(file_data)):
    num = file_data[i][1]
    newData.append(float(num))

n = len(newData)
newData.sort()

if n%2 == 0:
    median1 = float(newData[n//2]) 
    median2 = float(newData[n//2 - 1])

    median = (median1 +median2) /2

else:
    median = float(newData[n//2])

print("This is your required median :" , median)

    
