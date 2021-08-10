n,k=input().split()
l=list(map(int,input().split()))
def check_prime(nr):
    if(nr==1):
        return False
    if(nr==2):
        return True
    for i in range(2,nr):
        if nr%i==0:
            return False
    return True
l2=[]
for el in l:
    if check_prime(el)==True and el>=int(k):
        l2.append(el)
if len(l2)==0:
    print(-1)
else:
    print(min(l2))
