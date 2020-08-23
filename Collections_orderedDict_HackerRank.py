from collections import OrderedDict
n=int(input())
dic={}
dic=OrderedDict()
for i in range(n):
    a=input().split()
    b= int(a[-1])
    a= " ".join(a[:-1])
    if a in dic.keys():
        dic[a]=dic[a]+b
    else:
        dic[a]=b

for i in dic:
    print(i,dic[i])
