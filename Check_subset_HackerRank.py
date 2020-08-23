T=int(input())
for i in range(0,T):
    A=int(input())
    AL=list(map(int,input().split()))
    B=int(input())
    BL=list(map(int,input().split()))
    if(all(x in BL for x in AL)):
        print('True')
    else:
        print('False')
