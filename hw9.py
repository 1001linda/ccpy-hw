class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        nx = self.x + other.x
        ny = self.y + other.y
        nz = self.z + other.z
        return Vector(nx, ny, nz)
    def __sub__(self, other):
        nx = self.x - other.x
        ny = self.y - other.y
        nz = self.z - other.z
        return Vector(nx, ny, nz)
    def __eq__(self, other):
        if (self.x == other.x) and (self.y == other.y) and (self.z == other.z):
            return True
        else:
            return False
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    def __xor__(self, other):
        nx = self.y * other.z - self.z * other.y
        ny = self.z * other.x - self.x * other.z
        nz = self.x * other.y - self.y * other.x
        return Vector(nx, ny, nz)
    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "]"

def calc(a, b, command):
    if command == "add":
        return a + b
    elif command == "sub":
        return a - b
    elif command == "dot":
        return a * b
    elif command == "cross":
        return a ^ b
    elif command == "equal":
        return a == b


if __name__ == '__main__':
    n = int(input())
    list = []
    for i in range(n):
        x, y, z = input().split(" ")
        list.append(Vector(int(x), int(y), int(z)))
    while True:
        try:
            command = input().split(" ")
            a = list[int(command[0])-1]
            b = list[int(command[1])-1]
            print(calc(a, b, command[2]))
        except EOFError:
            exit()