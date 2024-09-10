def findgcd(a,b):
    if a == 0:
        return b
    else:
        return findgcd(b%a,a)
n = int(input())
for i in range(n):
    num = input().split(" ")
    print(findgcd(int(num[0]), int(num[1])))