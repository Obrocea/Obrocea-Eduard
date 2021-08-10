n=int(input())
l=[]
for i in range(n):
    el=float(input())
    l.append(el)
l2=[]
l.insert(0,0)
l.append(0)
for i in range(1,len(l)-1):
    if l[i-1]<l[i] and l[i+1]<l[i]:
        l2.append(l[i])
med=sum(l2)/len(l2)
cnt=0
for el in l:
    if el > med:
        cnt+=1
print(cnt)