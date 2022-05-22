import sys
from collections import Counter
file_name = sys.argv[0]

def readFile(file_name):
    words = []
    file = open(file_name+".txt", "r")
    count = Counter(word for line in file for word in line.split())
    file.close()
    words = count.most_common(20)
    words = [word[0] for word in words if word[1] == 20]
    file = open('popular_words.txt', 'w')
    for word in words:
        file.write("%s\n" % word)
    file.close()


readFile('index')
