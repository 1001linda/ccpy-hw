dg = {}
dn = {}
class stu(object):

    def i(self, id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade
        dg[int(id)] = int(grade)
        dn[int(id)] = name
    def d(self, id):
        del dg[int(id)]
        del dn[int(id)]
    def qg(self, id):
        print(dg[int(id)])
    def qn(self, id):
        print(dn[int(id)])

while True:
    try:
        stud = stu()
        inform = input().split()
        if inform[0] == "i":
            stud.i(inform[1],inform[2],inform[3])
        elif inform[0] == "d":
            stud.d(inform[1])
        elif inform[0] == "qg":
            stud.qg(inform[1])
        elif inform[0] == "qn":
            stud.qn(inform[1])
        elif inform[0] == "pg":
            dgg = sorted(dg.items(), key = lambda d:d[1])
            for key, value in dgg:
                print("{} {} {}".format(key,dn[int(key)],value) )
        elif inform[0] == "pi":
            dnn = sorted(dn.items(), key = lambda d:d[0])
            for key, value in dnn:
                print("{} {} {}".format(key,value,dg[int(key)]))
    except KeyError:
        print("ID",inform[1],"does not exist!")
    except TypeError:
        print("ID",inform[1],"does not exist!")
    except EOFError:
        exit()
