n = int(input())
s = set(map(int, input().split()))
N=int(input())
for i in range(N):
    S=input()
    S=S.split()
    if S[0]=='pop':
        try:
            s.pop()
        except:
            continue

    if S[0]=='remove':
        try:
            s.remove(int(S[1]))
        except:
            continue

    if S[0]=='discard':
        s.discard(int(S[1]))

print(sum(s))
