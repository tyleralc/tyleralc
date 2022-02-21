def read_csv(filename):  #opens and reads csv files 
    IDs=[]
    name=[]
    gender=[]
    fhand = open(filename, 'r', encoding= 'utf-8-sig')
    for line in fhand:
        line=line.rstrip().split(',')
        IDs.append(line[0])
        name.append(line[1])
        gender.append(line[2])
    students={x[0] : x[1:] for x in (IDs, name, gender)}
    return students

q2= read_csv("Students_Q2Q3.csv")
q3={}

for key, value in q2.items():
    value.append(key)
    q3[value.pop(0)]= value
print(q3)