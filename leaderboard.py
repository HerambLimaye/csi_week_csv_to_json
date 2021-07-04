import json

p = open('Day1.json', 'rb')

d = json.load(p)

leader = {}
leader2 = {}
name = []
score = []
tup = []

for k1, v1 in d.items():
    tot = 0
    for k2, v2 in d[k1].items():
        if k2 == 'name':
            continue
        #print(v2)
        tot += v2
    leader2[d[k1]['name']] = tot
    name.append(d[k1]['name'])
    score.append(tot)
    tup.append(tuple([d[k1]['name'], k1, tot]))

#for k1, v1 in leader.items():
    #print(k1, v1)


print(sorted(leader2, reverse=True, key=leader2.get))

print(sorted(tup, reverse=True, key=lambda a: a[2]))
lst = sorted(tup, reverse=True, key=lambda a: a[2])

print(lst)

for i in range(len(lst)):
    leader[i] = {'name': lst[i][0], 'email': lst[i][1], 'score': lst[i][2]}

print(leader)
with open('leaderboard.json', 'w', encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(leader, indent=4))