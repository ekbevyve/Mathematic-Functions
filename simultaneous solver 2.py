#this function simply returns the solutions to a simultaneous equation, given in the form of a list.
print("inputs are in the form [1]x + [2] = [3]y\n to receive answers of invalid implies the lines do not intersect, and there is no solutions")

eq1=[0,0,0]
eq1[0]=int(input("please enter x coeffiecient: "))
eq1[1]=int(input("please enter y coeffiecient: "))
eq1[2]=int(input("please enter constant: "))
print('this is for the second equation: ')
eq2=[0,0,0]
eq2[0]=int(input("please enter x coeffiecient: "))
eq2[1]=int(input("please enter y coeffiecient: "))
eq2[2]=int(input("please enter constant: "))

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

solutions=solve(eq1,eq2)
print("x = ",solutions[0],"\ny = ", solutions[1])
    
