def check_once(length):
    matrix = []
    row = []
    col = []
    addrow, addcol = 0, 0
    rerow, recol = 0, 0
    roww, coll= 0, 0
    for b in range(length):
        line = input().split()
        for c in range(length):
            line[c] = int(line[c])
        matrix.append(line)
    for i in range(length):
        roww = 0
        for j in range(length):
            roww = int(matrix[i][j] + roww)%2
        row.append(roww)
    print(row)
    for i in range(length):
        coll = 0
        for j in range(length):
            coll = int(matrix[j][i] + coll)%2
        col.append(coll)
    print(col)
    for i in range(length):
        addrow = addrow + int(row[i])
        addcol = addcol + int(col[i])
    if addrow == 0 and addcol == 0:
        print("OK")
    elif addrow == 1 and addcol ==1:
        for i in range(length):
            if row[i] == 1:
                rerow = i+1
            if col[i] == 1:
                recol = i+1
        print("Change bit"," ","(",rerow,",",recol,")",sep='' )
    else:
        print("Corrupt")


if __name__ == '__main__':
    while True:
        length = int(input())
        if length <= 0:
            break
        check_once(length)
        