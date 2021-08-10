from collections import defaultdict
d=defaultdict(list)
n,k=input().split()
n=int(n)
k=int(k)
l=list(map(int,input().split()))
j=int(0)
for el in l:
    d[j].append(el)
    j=j+1
    if j==n:
        j=0
for el in d:
    print(*d[el],sep=' ')
   