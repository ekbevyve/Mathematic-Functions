def componentforce(force, bearing):
    import math
    component=[]
    if bearing==360:
        bearing=0
    print('\nfor a force ',force,'N on a bearing of ',bearing,'from the vertical:')
    if bearing<=90:
        angle=90-bearing
        up=True
        right=True
    elif bearing>90 and bearing<=180:
        angle=bearing-90
        up=False
        right=True
    elif bearing>180 and bearing<=270:
        angle=270-bearing
        up=False
        right=False
    elif bearing>270 and bearing<=360:
        angle=bearing-270
        up=True
        right=False
    #horizontal component:
    comp=math.cos(angle)*force
    if right==False:
        comp=-comp
    component.append(comp)
    comp=math.sin(angle)*force
    if right==False:
        comp=-comp
    component.append(comp)
    print(component[0],'i +', component[1],'j')
    return(component)
theta=[0,45,90,135,180,225,270,315,360]
for i in range(len(theta)):
    componentforce(50,theta[i])
    
