#this program aims to provide the equation of a circle given 3 coordinates.
def getcoordinate():
    coordinate=[]
    coordinate.append(int(input('please enter the x coordinate: ')))
    coordinate.append(int(input('please enter the y coordinate: ')))
    return coordinate

def perpbisector(cord1,cord2):
    lineeq=[0,0,1]
    #list containing 3 values for m x + c = y
    m=(cord1[1]-cord2[1])/(cord1[0]-cord2[0])
    perpm=-1/m
    lineeq[0]=perpm
    midpoint=[(cord1[0]+cord2[0])/2,(cord1[1]+cord2[1])/2]
    lineeq[1]=midpoint[1]-(perpm*midpoint[0])
    return lineeq

def solve(e1,e2):
    xcoeff=(e1[0]/e1[2])-(e2[0]/e2[2])
    const=(e2[1]/e2[2])-(e1[1]/e1[2])
    if xcoeff!= 0:
        solutionx=const/xcoeff
        solutiony=((e1[0])*solutionx +e1[1])/ e1[2]
    else:
        solutionx = "invalid"
        solutiony = "invalid"
    return solutionx, solutiony

def distance(c1,c2):
    distance=((c1[0]-c2[0])**2+(c1[1]-c2[1])**2)**0.5
    return distance
print('this application aims to find the equation of a circle given 3 coordinates \n\nplease enter x/y values for the first one:')
cord1=getcoordinate()

print('\n\nplease enter values for the next coordinate:')
cord2=getcoordinate()

print('\n\nplease enter values for the final coordinate:')
cord3=getcoordinate()

line1=perpbisector(cord1,cord2)
line2=perpbisector(cord2,cord3)

center=solve(line1,line2)
r=(distance(cord1,center))**2
#forming our circle list eq in the form (x-a)^2 + (y-b)^2 = r^2
circleq=[]
circleq.append(center[0])
circleq.append(center[1])
circleq.append(r)

print("\n\nthe equation is: (x-",circleq[0],")^2 + (y-",circleq[1],") =",r)
