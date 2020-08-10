import string
def alph(i,n):
    a= list(string.ascii_lowercase)
    if i>1:
        return a[n]+"-"+alph(i-1,n-1)+"-"+a[n]
    else:
        return a[n]

def print_rangoli(size):
    # your code goes here
    
    x=size+(size-1)*3
    y=size*2-1
    u=int(y/2)+1
    for i in range(1,u+1):
        m=int((x-(i*4-3))/2)
        s=alph(i,size-1)
        rangoli="-"*m+s+"-"*m
        print(rangoli)
    for i in range(u-1,0,-1):
        m=int((x-(i*4-3))/2)
        s=alph(i,size-1)
        rangoli="-"*m+s+"-"*m
        print(rangoli)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
