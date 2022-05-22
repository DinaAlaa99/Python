import math

def findDistance(p1,p2):

   distance = math.sqrt(((p2[0]-p1[0])**2)+((p2[1]-p1[1])**2))
   return distance


p1 = [2, 0]
p2 = [6, 2]
distance = findDistance(p1,p2)
print(distance)
