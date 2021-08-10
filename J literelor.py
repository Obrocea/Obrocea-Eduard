inc,sf,m,n=input().split()
m=int(m)
n=int(n)
inc=inc.lower()
sf=sf.lower()
mai_mic=int(0)
interval=int(0)
mai_mare=int(0)
l=input().split()
for el in l:
    el=el.lower()
    if el[0]==inc and el[-1]==sf:
        if len(el)<m:
            mai_mic=mai_mic+1
        elif len(el)>=m and len(el)<n:
            interval=interval+1
        elif len(el)>=n:
            mai_mare=mai_mare+1
print(mai_mic,interval,mai_mare)