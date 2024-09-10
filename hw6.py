di = { }
while True:

    try:
        inform = input().split()
        if inform[0] == "i":
            di[inform[1]] = int(inform[2])
        elif inform[0] == "d":
            del di[inform[1]]
        elif inform[0] == "q":
            print(di[inform[1]])
        elif inform[0] == "p":
            dii = sorted(di.items(), key = lambda d:d[1], reverse=True)
            for key, value in dii:
                print("{} {}".format(key,value))

    except KeyError:
        print(inform[1],"does not exist!")
    except TypeError:
        print(inform[1],"does not exist!")
    except EOFError:
        exit()

