import sys
import csv

def transpose(in_file, out_file):
    file=[]
    fhand = open(in_file, 'r', encoding= 'utf-8-sig')
    for line in fhand:
        line=line.rstrip().split(',')
        file.append(line)

    transposed = []
    for i in range(4):
        transposed.append([row[i] for row in file])
        
    with open(out_file, 'w', newline='') as csvfile:
        csv_writ= csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writ.writerows(transposed)

transpose(str(sys.argv[1]),  str(sys.argv[2]))