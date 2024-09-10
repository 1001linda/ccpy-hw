import hashlib

f = open("CPPY_hw03.txt", "r")
line = f.readlines()
print(len(line))
for i in range(len(line)):
    line2 = (line[i] +"110304029")
    a = hashlib.md5(line2.encode("utf-8")).hexdigest()
    print(a)
f.close()