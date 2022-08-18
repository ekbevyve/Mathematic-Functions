#This code aims to read a file of SUVAT equations, then select and use the valid choice. Provided inputs of SUVAT

#defining the dictinary and printing instructions to user
variables={}
print('For this function to work accurately, please enter variables by the standard SUVAT and ensure acceleration is modelled as constant \n that is: \ns= distance\nu= initial speed\nv=final speed\na= accelleration\nt=time taken\n')
#collecting SUVAT values
suvat=['s','u','v','a','t']
loop=True

#validity check loop: to ensure users enter valid inputs
for i in range(len(suvat)):
    #loop here ensuring user enters 1 or 0
    while loop==True:
        print('Do you know the value for ',suvat[i],'? (1=yes, 0=no)')
        ans=input()
        if ans=='0' or ans=='1':
            loop=False
        else:
            print('Please enter 1 or 0')
    if ans=='1':
        variables[suvat[i]]=input('what is the value? ')
    #resetting variables to ensure following repetitions all work
    ans=''
    loop=True

#after constructing a dictionary of known values, program will read equations from external file and match all usable ones
knownvalues=list(variables)
file = open("SUVAT_equations.txt",'r')
line=file.readline()
equations=[]
while line!='':
    ans=0
    for i in range(len(knownvalues)):
        if knownvalues[i] in line:
            ans+=1
    #we have enough known values to use this equation, so appending the list of usable equations
    if ans>=3:
        equations.append(line)
    line=file.readline()

#now we have the known values, and the equations: all we do now is rearrange and solve them:)
