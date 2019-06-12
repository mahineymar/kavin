num=int(input())
x=list(map(int,input().split()))
y=sorted(x)[::-1]
z=""
if(x==[0]*num):
    print("0")
else:
    for i in y:
        z=z+str(i)
    print(int(z)) 
