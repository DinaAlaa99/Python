def divideString(string):

    if (len(string) % 2 == 0):
        front = slice(0, len(string)//2)
        back = slice(len(string)//2, len(string))

    else:
        front = slice(0, (len(string)//2)+1)
        back = slice((len(string)//2)+1, len(string))

    print('('+string[front]+'-front + '+string[back]+'-front) + ' +
          '('+string[front]+'-back + '+string[back] + '-back)')
    


divideString("ab")
