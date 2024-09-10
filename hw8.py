
d = {}
class stu():
    
    def i(self, id, name, grade, special):
        self.id = int(id)
        self.name = name
        self.grade = int(grade)
        self.special = int(special)
        d[int(id)] = [int(id), name, int(grade), int(special)]
    def d(self, id):
        del d[int(id)]
    def qg(self, id):
        print(d[int(id)][2])
    def qn(self, id):
        print(d[int(id)][1])
    def pg(self):
        dg = sorted(d.items(), key = lambda d:d[0])
        for key, value in dg:
            print("{} {} {}".format(key, value[1], value[2]))
    def pm(self):
        dm ={key:value for key, value in sorted(d.items(), key = lambda d:d[0])} 
        for key in dm:
            if int(dm[key][3]) == 1:
                c = min(max(int(dm[key][2])*5/2-20, 0), 100)
                print("{} {} {}".format(dm[key][0], dm[key][1], c))    
            elif int(dm[key][3]) == 0:
                c = min(max(int(dm[key][2])*3/2-10, 0), 100)
                print("{} {} {}".format(dm[key][0], dm[key][1], c))
        
        

while True:
    try:
        stud = stu()
        inform = input().split()
        if inform[0] == "i":
            stud.i(int(inform[1]),inform[2],int(inform[3]),int(inform[4]))
        elif inform[0] == "d":
            stud.d(int(inform[1]))
        elif inform[0] == "qg":
            stud.qg(int(inform[1]))
        elif inform[0] == "qn":
            stud.qn(int(inform[1]))
        elif inform[0] == "pg":
            stud.pg()
        elif inform[0] == "pm":
            
            stud.pm()
    except KeyError:
        print("ID",inform[1],"does not exist!")
    except TypeError:
        print("ID",inform[1],"does not exist!")
    except EOFError:
        exit()
