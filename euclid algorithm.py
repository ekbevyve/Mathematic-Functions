#euclids algorithm function
print('this program aims to do my first year uni math for me\n\nplease enter two numbers, a and b, to begin')
a=int(input('a = '))
b=int(input('b = '))
r= 1
#the following if statement ensures a is always the bigger of the two entries.
if a<b:
    c=b
    b=a
    a=c
#such a long tedious process summarised in 4 lines in a while loop :')
while r!=0:
    q=a//b
    r=a%(q*b)
    print(a," = ",q,"(",b,") +",r)
    a=b
    b=r

