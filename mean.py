import csv
with open ("SOCR-HeightWeight.csv" , newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
newData = []
for i in range (len(file_data)):
    num = file_data[i][1]
    newData.append(float(num))

n = len(newData)

sum = 0
for x in newData:
    sum += x

mean  = sum/n


print("This is Your required mean : " , mean)

