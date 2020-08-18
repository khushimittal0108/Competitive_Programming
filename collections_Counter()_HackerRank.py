# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X=int(input())
l=list(map(int,input().split()))
cnt = Counter(l)
N=int(input())
l2=[]
price=0
for i in range(N):
    a=list(map(int,input().split()))
    if cnt[a[0]]>0:
        price=price+a[1]
        cnt[a[0]]=cnt[a[0]]-1
   
print(price)
