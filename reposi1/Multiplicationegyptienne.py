x=int(input("x= "))
y=int(input("y= "))

result=0

while(y>0):
    if(y%2==0):
        x=x+x
        y=y/2
    else:
        result=result+x
        y=y-1

print(result)