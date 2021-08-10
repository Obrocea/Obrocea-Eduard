n=int(input())
s=input().strip()
t00=int(0)
t01=int(0)
t10=int(0)
t11=int(0)
for i in range(0,n-1,2):
    if s[i]=='0' and s[i+1]=='0':
        t00=t00+1
    elif s[i]=='0' and s[i+1]=='1':
        t01=t01+1
    elif s[i]=='1' and s[i+1]=='0':
        t10=t10+1
    elif s[i]=='1' and s[i+1]=='1':
        t11=t11+1
r1=max(t10,t11,t01,t00)/min(t10,t11,t01,t00)
print("%.2f"%r1,end=' ')
t1=s.count('1')
t0=s.count('0')
if t1>t0:
    r2=t1/t0
else:
    r2=t0/t1
print("%.2f"%r2)
if r1>1.1 or r2>1.1:
    print('0')
elif r1<=1.1 and r2<=1.1:
    print('1')
