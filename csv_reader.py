import csv
file = "CSV00001_B_Links.txt"
x = []
y = []

def Replace(str1):
    maketrans = str1.maketrans
    final = str1.translate(maketrans(',.', '.,', ' '))
    return final.replace(',', ", ")

with open(file, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='\\')
    for row in reader:
        #print(';'.join(row))
        x.append(Replace(row[0]))
        y.append(Replace(row[1]))

print("X = " + ','.join(x))
print("Y = " + ','.join(y))
        
