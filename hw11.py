class shape():
    def __init__(self, perimeter, area):
        self.perimeter = int(perimeter)
        self.area = int(area)
    def __eq__(self, other):
        return self.area == other.area
    def __gt__(self, other):
        return self.perimeter > other.perimeter
    def __lt__(self, other):
        return self.perimeter < other.perimeter
    def __add__(self, other):
        scircle = self.area + other.area
        ssquare = self.perimeter + other.perimeter
        striangle = scircle + ssquare
        if first[0] == "circle":
            return scircle
        elif first[0] == "square":
            return ssquare
        elif first[0] == "triangle":
            return striangle

class column():
    def __init__(self, perimeter, area, hieght):
        self.perimeter = int(perimeter)
        self.area = int(area)
        self.hieght = int(hieght)
    def __eq__(self, other):
        return self.area*self.hieght == other.area*other.hieght
    def __gt__(self, other):
        return self.perimeter*self.hieght > other.perimeter*other.hieght
    def __lt__(self, other):
        return self.perimeter*self.hieght < other.perimeter*other.hieght
    def __add__(self, other):
        scircle = self.perimeter*self.hieght + other.perimeter*other.hieght
        ssquare = self.area*self.hieght + other.area*other.hieght
        striangle = scircle + ssquare
        print(scircle, ssquare, striangle)
        if first[0] == "circleColumn":
            return scircle
        elif first[0] == "squareColumn":
            return ssquare
        elif first[0] == "triangleColumn":
            return striangle

while True:
    try:
        first = input().split()
        op = input()
        second = input().split()
        if first[0] == "circle" or "square" or "triangle":
            a = shape(int(first[1]), int(first[2]))
            b = shape(int(second[1]), int(second[2]))
            if op == "==":
                print(a == b)
            elif op == ">":
                print(a > b)
            elif op == "<":
                print(a < b)
            elif op == "+":
                print(a + b)
        elif first[0] == "circleColumn" or "squareColumn" or "triangleColumn":
            a = column(int(first[1]), int(first[2]), int(first[3]))
            b = column(int(second[1]), int(second[2]), int(second[3]))
            if op == "==":
                print(a == b)
            elif op == ">":
                print(a > b)
            elif op == "<":
                print(a < b)
            elif op == "+":
                print(a + b)
    except EOFError:
        exit()