# Enter your code here. Read input from STDIN. Print output to STDOUT
inp=input().split()
n=int(inp[0])
m=int(inp[1])
s='.|.'
for i in range(1,int(n/2)+1):
    f=2*i-1
    a=int((m-f*3)/2)
    x=a*'-'+f*s+a*'-'
    print(x)
y=int((m-7)/2)
print(y*'-'+'WELCOME'+y*'-')
for i in range(int(n/2),0,-1):
    f=2*i-1
    a=int((m-f*3)/2)
    x=a*'-'+f*s+a*'-'
    print(x)
