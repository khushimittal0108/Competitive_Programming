#python2 
from collections import namedtuple
n=int(input())
student=namedtuple('student',raw_input())
f=int([i for i in range(4) if student._fields[i]=='MARKS'][0])
l=[int(raw_input().split()[f]) for i in range(n)]  
print('%.2f'%(float(sum(l))/float(n)))
