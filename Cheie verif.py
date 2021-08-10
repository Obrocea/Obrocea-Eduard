a = int(input())
b = int(input())
c=0
a=a*b
while a>10:
    while a>0:
        b=a%10
        a=(a-b)//10
        c=c+b
    a=c
    c=0
print(a)