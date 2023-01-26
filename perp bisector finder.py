#this program aims to find a perpendicular bisector of two coordinates
def getcoordinate():
    coordinate=[]
    coordinate.append(int(input('please enter the x coordinate: ')))
    coordinate.append(int(input('please enter the y coordinate: ')))
    return coordinate
print('this program aims to find a perpendicular bisector of two coordinates\n\nplease enter values for the first coordinate:')
coord1=getcoordinate()
print('\n\nplease enter values for the next coordinate:')')
coord2=getcoordinate()
def perpbisector(cord1,cord2):
    lineeq=[1,0,0]
    #list containing 3 values for y = m x + c
    m=(cord1[1]-cord2[1])/(cord1[0]-cord2[0])
    perpm=-1/m
    lineeq[1]=perpm
    midpoint=[(cord1[0]+cord2[0])/2,(cord1[1]+cord2[1])/2]
    lineeq[2]=midpoint[1]-(perpm*midpoint[0])
    return lineeq
perpbi=perpbisector(coord1,coord2)
print("The perpendicular bisector equation is: y = ",perpbi[1],"x + ",perpbi[2])

