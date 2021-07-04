import json
import csv

data={}
with open('reg2.csv') as csvfile1 :
    csvread=csv.DictReader(csvfile1)
    for rows in csvread:
        key = rows['Username']
        data[key] = {}


with open('ER.csv') as csvfile1 :
    csvread=csv.DictReader(csvfile1)
    for rows in csvread:
        key = rows['Email address']
        if key not in data:
            data[key] = {}

#with open('Day1.json', 'w', encoding='utf-8') as jsonf:
#    jsonf.write(json.dumps(data, indent=4))


list_tuples=[]
with open('reg2.csv') as csvfile2:
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
        data[x]['Escape Room']=0
        data[x]['Blind Code']=0


#with open('Day1.json', 'w', encoding='utf-8') as jsonf:
#    jsonf.write(json.dumps(data, indent=4))

list_tuples=[]
with open('ER.csv') as csvfile2:
    csv_reader = csv.reader(csvfile2,delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count=line_count+1
        else:
            tuple=(row[1],row[2])
            list_tuples.append(tuple)

key_no=0
for (x,y) in list_tuples:
    if x in data:
        data[x]['name']=y
        data[x]['Escape Room']=1


list_tuples=[]
with open('blindcode.csv') as csvfile2:
    csv_reader=csv.reader(csvfile2,delimiter=',')
    line_count=0
    for row in csv_reader:
        if line_count==0:
            line_count=line_count+1
        else:
            tuple=(row[0],row[6])
            list_tuples.append(tuple)

key_no=0
for (x,y) in list_tuples:
    if x in data:
        data[x]['name']=y
        data[x]['Blind Code']=1


for row in data:
    data[row]['Kickstart your GitHub Page']=0
    data[row]["A new language is just a 'hello world' away..."]=0
    data[row]["It's all about the Perfect Layout"]=0
    data[row]["Bas bajna chahiye Gaana"]=0
    data[row]["Sort it Out!"]=0

    data[row]['Get set, go with your logo!']=0
    data[row]["Privacy is Priority!"]=0
    data[row]["Data will TALK to you if, You are willing to LISTEN! ~ Jim Bergeson"]=0
    data[row]["Create a Reminder List"]=0

    data[row]['Learn....Build....Share...']=0
    data[row]["Bring a Chat Bot to Life!"]=0
    data[row]["Fit Step Go!"]=0
    data[row]["All you need is Maps"]=0
    data[row]["Bootstrap for everyone"] = 0

    data[row]['System Authenticator']=0
    data[row]["Recreation Time!"]=0
    data[row]["Flex your GitHub activity"]=0
    data[row]["Snap Time"]=0
    data[row]["Oh Dinosaur! We really love you"] = 0

    data[row]['Think Automate']=0
    data[row]["Gift for your loved ones"]=0
    data[row]["HeadStart your StartUp"]=0
    data[row]['"Yes, but chess can also be.....Beautiful" - Beth Harmon']=0
    data[row]["Confused Unga Bunga"] = 0

    data[row]['Let the InCome come in']=0
    data[row]["Gadbad Ghotala"]=0
    data[row]["Event Code Decode"]=0
    data[row]["Memory Loss"]=0
    data[row]["Meet & Greet"] = 0
    
    # data[row]['Escape Room']=0
    # data[row]["Blind Code"]=0



with open('Day1.json', 'w', encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(data, indent=4))


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


with open('Day2.csv') as csvfile4:
    csv_reader=csv.reader(csvfile4,delimiter=',')
    line_count=0
    for rowa in csv_reader:
        if line_count==0:
            line_count=line_count+1
        else:
            for row in data:
                if rowa[1]==row and rowa[2]=='Get set, go with your logo!':
                    data[row]['Get set, go with your logo!'] = 1
                if rowa[1] == row and rowa[2] == "Privacy is Priority!":
                    data[row]["Privacy is Priority!"] = 1
                if rowa[1] == row and rowa[2] == "Data will TALK to you if, You are willing to LISTEN! ~ Jim Bergeson":
                    data[row]["Data will TALK to you if, You are willing to LISTEN! ~ Jim Bergeson"] = 1
                if rowa[1] == row and rowa[2] == "Create a Reminder List":
                    data[row]["Create a Reminder List"] = 1



with open('Day1.json', 'w', encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(data, indent=4))


# with open('Day3.csv') as csvfile5:
#     csv_reader=csv.reader(csvfile5,delimiter=',')
#     line_count=0
#     for rowa in csv_reader:
#         if line_count==0:
#             line_count=line_count+1
#         else:
#             for row in data:
#                 if rowa[1]==row and rowa[2]=='Learn....Build....Share...':
#                     data[row]['Learn....Build....Share...'] = 1
#                 if rowa[1] == row and rowa[2] == "Bring a Chat Bot to Life!":
#                     data[row]["Bring a Chat Bot to Life!"] = 1
#                 if rowa[1] == row and rowa[2] == "Fit Step Go!":
#                     data[row]["Fit Step Go!"] = 1
#                 if rowa[1] == row and rowa[2] == "All you need is Maps":
#                     data[row]["All you need is Maps"] = 1
#                 if rowa[1] == row and rowa[2] == "Bootstrap for everyone":
#                     data[row]["Bootstrap for everyone"] = 1
#
#
# with open('Day1.json', 'w', encoding='utf-8') as jsonf:
#     jsonf.write(json.dumps(data, indent=4))


# with open('Day4.csv') as csvfile6:
#     csv_reader=csv.reader(csvfile6,delimiter=',')
#     line_count=0
#     for rowa in csv_reader:
#         if line_count==0:
#             line_count=line_count+1
#         else:
#             for row in data:
#                 if rowa[1]==row and rowa[2]=='System Authenticator':
#                     data[row]['System Authenticator'] = 1
#                 if rowa[1] == row and rowa[2] == "Recreation Time!":
#                     data[row]["Recreation Time!"] = 1
#                 if rowa[1] == row and rowa[2] == "Flex your GitHub activity":
#                     data[row]["Flex your GitHub activity"] = 1
#                 if rowa[1] == row and rowa[2] == "Snap Time":
#                     data[row]["Snap Time"] = 1
#                 if rowa[1] == row and rowa[2] == "Oh Dinosaur! We really love you":
#                     data[row]["Oh Dinosaur! We really love you"] = 1
#
#
# with open('Day1.json', 'w', encoding='utf-8') as jsonf:
#     jsonf.write(json.dumps(data, indent=4))


with open('WeekLong.csv') as csvfile7:
    csv_reader=csv.reader(csvfile7,delimiter=',')
    line_count=0
    for rowa in csv_reader:
        if line_count==0:
            line_count=line_count+1
        else:
            for row in data:
                if rowa[1]==row and rowa[2]=='Think Automate':
                    data[row]['Think Automate'] = 1
                if rowa[1] == row and rowa[2] == "Gift for your loved ones":
                    data[row]["Gift for your loved ones"] = 1
                if rowa[1] == row and rowa[2] == "HeadStart your StartUp":
                    data[row]["HeadStart your StartUp"] = 1
                if rowa[1] == row and rowa[2] == '"Yes, but chess can also be.....Beautiful" - Beth Harmon':
                    data[row]['"Yes, but chess can also be.....Beautiful" - Beth Harmon'] = 1
                if rowa[1] == row and rowa[2] == "Confused Unga Bunga":
                    data[row]["Confused Unga Bunga"] = 1
                if rowa[1]==row and rowa[2]=='Let the InCome come in':
                    data[row]['Let the InCome come in'] = 1
                if rowa[1] == row and rowa[2] == "Gadbad Ghotala":
                    data[row]["Gadbad Ghotala"] = 1
                if rowa[1] == row and rowa[2] == "Event Code Decode":
                    data[row]["Event Code Decode"] = 1
                if rowa[1] == row and rowa[2] == "Memory Loss":
                    data[row]["Memory Loss"] = 1
                if rowa[1] == row and rowa[2] == "Meet & Greet":
                    data[row]["Meet & Greet"] = 1


with open('Day1.json', 'w', encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(data, indent=4))