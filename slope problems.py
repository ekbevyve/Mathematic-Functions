#code to solve problems relating to a slope
print('this code will solve a slope problem, assuming the object is on the point of slipping\n')
#this function will ensure all inputs are computable numbers
import math
def validcheck(validity):
    try:
        # Convert it into float
        val = float(validity)
        valid=True
        validity=float(validity)
    except ValueError:
        if validity!='':
            print("invalid input!! please ensure you've entered a valid number, sunshine :(\n")
            valid=False
            validity=''
        else:
            valid=True
    return valid, validity
#here i am getting my first 3 inputs: mu, w, and theta.
valid=False
while valid==False:
    mu = input('\nwhat is the coefficient of friction? \ntop tip: simply enter if there is none given \nmu= ')
    mulist=validcheck(mu)
    valid=mulist[0]
mu=mulist[1]
valid=False
while valid==False:
    w = input('\nwhat is the mass of the object? (in kilograms please muffin) \ntoptip: simply enter if there is none given cutie \n w= ')
    wlist=validcheck(w)
    valid=wlist[0]
w=wlist[1]
valid=False
while valid==False:
    theta= input('\nwhat is the angle of the slope? (in degrees pls hunnyluv) \nyet again: simply enter if there is none given cherrypie \n θ= ')
    thetalist=validcheck(theta)
    valid=thetalist[0]
theta=thetalist[1]
#verifying theta is not bigger than 90 cux thats not a slope thats wild as hell
if thetalist[1]!='':
    if thetalist[1]>=90:
        valid=False
        hold=thetalist
    while valid==False:
        if hold[1]>=90:
            print("oops! the angle of the slope can't be bigger than 90 degrees, sugarplum~ ")
        theta= input('\nwhat is the angle of the slope? hint: simply enter if there is none given sweetcheeks \n θ= ')
        hold=validcheck(theta)
        if hold[0]==True:
            thetalist=hold
            if hold[1]<90:   
                valid=thetalist[0]
                theta=thetalist[1]
    theta=math.radians(theta)
valid=False
while valid==False:
    g= input('what are we taking g to be \n g= ')
    glist=validcheck(g)
    if glist[1]!='':
        valid=glist[0]
g=glist[1]
print('according to my calculations..')
#here im calculating theta and mu which are interchangeably solveable
solve=0
if mu == '' and theta!='':
    mu=math.tan(theta)
if theta == '' and mu!='':
    theta=math.atan(mu)
#here i am working out if i need any more info before i can whip out some mad maths frfr
if theta!='':
    solve+=1
if mu !='':
    solve+=1
if w !='':
    solve+=1
#if solve==3: solve all here (work in progress)
if solve==3:
    f=math.sin(theta)*w*g
    r=math.cos(theta)*w*g
    fric=mu*math.cos(theta)*w*g
    print('\nIMPORTANT! if you input a value for all of the above three, the previously assumed scenario may not be true: \nthat is that the box was on the point of slipping. \nas a result of this, friction is not equal to the weight down the slope.\n \nThe solutions are as follows:\nmu = ',mu,'\ntheta (radians) = ',theta,'\ntheta (degrees) = ',math.degrees(theta),'\nmass = ',w,'\nweight down the slope = ',f,'\nreaction force between box and slope = ',r,'\nfrictional force = ',fric,'\nweight component perpendicular to slope = ',r)
if solve<3 or w=='':
    #since i only have one piece of info, or no mass i need more in order do whip out some mad maths frfr
    print('\nI need more information to solve this, sorry sugarpie...')
    valid=False
    while valid==False:
        f = input('\nwhat is the force of the object down the slope? (in newtons please sugarflake) \ntoptip: simply enter if there is none given buttercup \n F= ')
        flist=validcheck(f)
        valid=flist[0]
    f=flist[1]
    valid=False
    if f=='':
        while valid==False:
            fric = input('\nwhat is the friction force? (in newtons please muffin) \ntoptip: simply enter if there is none given banana \n Fr= ')
            frlist=validcheck(fric)
            valid=frlist[0]
        fric=frlist[1]
    else:
        fric=f
    valid=False
    while valid==False:
        r = input('\nwhat is the reaction force of the object? (in newtons again please princess) \ntoptip: simply enter if there is none given applepie \n r= ')
        rlist=validcheck(r)
        valid=rlist[0]
    r=rlist[1]
    if fric=='' or f=='':
        if fric!='':
            f=fric
        if f!='':
            fric=f
    if fric!='':
        solve+=1
    if f !='':
        solve+=1
    if r !='':
        solve+=1
    if solve>=3:
        print('\nok babycakes... i hope you are ready for the mathematicals...')
        if w=='' and theta!='':
            if f!='' and w=='':
                w=f/(g*math.sin(theta))
            if r!='' and w=='':
                w=f/(g*math.cos(theta))
        if theta=='' and w!='':
            if f!='' and theta=='':
                theta=math.asin(f/(w*g))
            if r!='' and theta=='':
                theta=math.acos(r/(w*g))
        if theta=='' and w=='':
            mu=fric/r
            theta=math.atan(mu)
            w=(f+fric)/(g*(math.sin(theta)+math.cos(theta)))
        #solve all here
        if mu == '':
            mu=math.tan(theta)
        if f == '':
            f=math.sin(theta)*w*g
        if r == '':
            r=math.cos(theta)*w*g
        if fric =='':
            fric=mu*math.cos(theta)*w*g
        print('\nThe solutions are as follows:\nmu = ',mu,'\ntheta (radians) = ',theta,'\ntheta (degrees) = ',math.degrees(theta),'\nmass = ',w,'\nweight down the slope = ',f,'\nreaction force between box and slope = ',r,'\nfrictional force = ',fric,'\nweight component perpendicular to slope = ',r)
    else:
        print('\nsorry munchkin I am not sure how to do that:(')
