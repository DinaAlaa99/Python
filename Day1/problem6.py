def findCharLocation(string, char):
    res = []
    for i in range(0, len(string)):
        if string[i] == char:
            res.append(i)
    print(res)

findCharLocation("iti",'i')