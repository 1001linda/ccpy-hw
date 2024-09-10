d = {}
di = input()
value = di.split(',')
for i in range(len(value)):
    key = i+1
    d[key] = value[i]

while True:
    try:
        word = input()
    except EOFError:
        exit()
    
    samealp = []
    if word in d.values():
        alp = word[0].upper()
        for c in d.values():
            if word[0] == c[0]:
                samealp.append(c)
        samealp.sort()
        for i in samealp:
            if word == i:
                o = samealp.index(i)+1
                print(alp , o)
                break
    else:
        print("NOT FOUND")