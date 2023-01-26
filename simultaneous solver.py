#this program aims to solve simultaneous equations between 2 straight lines
#list inputs are in the form [1]x + [2]y = [3]
print("inputs are in the form [1]x + [2]y = [3]")
eq1=[0,0,0]
eq1[0]=int(input("please enter x coeffiecient: "))
eq1[1]=int(input("please enter y coeffiecient: "))
eq1[2]=int(input("please enter constant: "))
print('this is for the second line: ')
eq2=[0,0,0]
eq2[0]=int(input("please enter x coeffiecient: "))
eq2[1]=int(input("please enter y coeffiecient: "))
eq2[2]=int(input("please enter constant: "))
#this function simply reads my listed equations in a legible way, and rearranges it for my user. It assumes all coefficients are positive.
def read1(eq):
    print(eq[0],"x + ",eq[1],"y = ",eq[2])
    print(eq[0],"x - ",eq[2]," = -",eq[1],"y")
    print("(",eq[0],"x - ",eq[2],")/ -",eq[1]," = y")
#the following function will reassign the list values to make for easier solving
def fix(eq):
    eq[2]=-1*eq[2]
    eq[1]=-1*eq[1]
#we will be putting the rearranging then equating method into python
def solvex(e1,e2):
    print("(",e1[0],"x + ",e1[2],")/",e1[1]," = y")
    print("(",e2[0],"x + ",e2[2],")/",e2[1]," = y")
    print("(",e1[0],"x + ",e1[2],")/",e1[1]," = (",e2[0],"x + ",e2[2],")/",e2[1])
    print(e1[0]/e1[1],"x + ",e1[2]/e1[1]," = ",e2[0]/e2[1],"x + ",e2[2]/e2[1])
    xcoeff=(e1[0]/e1[1])-(e2[0]/e2[1])
    const=(e2[2]/e2[1])-(e1[2]/e1[1])
    print(xcoeff,'x =',const)
    print("so x = ", const/xcoeff)
    solution=const/xcoeff
    return solution
read1(eq1)
read1(eq2)
fix(eq1)
fix(eq2)
x=solvex(eq1,eq2)

y=((eq1[0])*x +eq1[2])/ eq1[1]
print('and y = ', y)
