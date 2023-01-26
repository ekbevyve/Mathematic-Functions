#this program aims to find the distance between 2 points.
def getcoordinate():
    coordinate=[]
    coordinate.append(int(input('please enter the x coordinate: ')))
    coordinate.append(int(input('please enter the y coordinate: ')))
    return coordinate
def distance(c1,c2):
    distance=((c1[0]-c2[0])**2+(c1[1]-c2[1])**2)**0.5
    return distance
print('this program aims to find the distance between two points:\n\n')
print('please enter values for the first coordinate:')
cord1=getcoordinate()
print('\n\nplease enter values for the second coordinate:')
cord2=getcoordinate()
dis=distance(cord1,cord2)
print('the distance between these two is ',dis,' units')
