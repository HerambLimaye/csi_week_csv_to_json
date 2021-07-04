import json
import csv

data={}
with open('Day1.csv') as csvfile1 :
    csvread=csv.DictReader(csvfile1)
    for rows in csvread:
        key = rows['Email address']
        data[key] = {}


#with open('Day1.json', 'w', encoding='utf-8') as jsonf:
#    jsonf.write(json.dumps(data, indent=4))


list_tuples=[]
with open('reg.csv') as csvfile2:
    csv_reader=csv.reader(csvfile2,delimiter=',')
    line_count=0
    for row in csv_reader:
        if line_count==0:
            line_count=line_count+1
        else:
            tuple=(row[1],row[3])
            list_tuples.append(tuple)

key_no=0
for (x,y) in list_tuples:
    if x in data:
        data[x]['name']=y


#with open('Day1.json', 'w', encoding='utf-8') as jsonf:
#    jsonf.write(json.dumps(data, indent=4))


for row in data:
    data[row]['Kickstart your GitHub Page']=0
    data[row]["A new language is just a 'hello world' away..."]=0
    data[row]["It's all about the Perfect Layout"]=0
    data[row]["Bas bajna chahiye Gaana"]=0
    data[row]["Sort it Out!"]=0


#with open('Day1.json', 'w', encoding='utf-8') as jsonf:
#    jsonf.write(json.dumps(data, indent=4))


with open('Day1.csv') as csvfile3:
    csv_reader=csv.reader(csvfile3,delimiter=',')
    line_count=0
    for rowa in csv_reader:
        if line_count==0:
            line_count=line_count+1
        else:
            for row in data:
                if rowa[1]==row and rowa[2]=='Kickstart your GitHub Page':
                    data[row]['Kickstart your GitHub Page'] = 1
                if rowa[1] == row and rowa[2] == "A new language is just a 'hello world' away...":
                    data[row]["A new language is just a 'hello world' away..."] = 1
                if rowa[1] == row and rowa[2] == "It's all about the Perfect Layout":
                    data[row]["It's all about the Perfect Layout"] = 1
                if rowa[1] == row and rowa[2] == "Bas bajna chahiye Gaana":
                    data[row]["Bas bajna chahiye Gaana"] = 1
                if rowa[1] == row and rowa[2] == "Sort it Out!":
                    data[row]["Sort it Out!"] = 1


with open('Day1.json', 'w', encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(data, indent=4))