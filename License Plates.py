from sys import stdin
s='AB,AR,AG,B,BC,BH,BN,BT,BV,BR,BZ,CS,CL,CJ,CT,CV,DB,DJ,GL,GR,GJ,HR,HD,IL,IS,IF,MM,MH,MS,NT,OT,PH,SM,SJ,SB,SV,TR,TM,TL,VS,VL,VN'
l=[]
l=s.split(',')
s=set()
l2=[]
l3=[]
for line in stdin:
    if line=='':
        break
    l2.append(line)




l2.remove(l2[-1])

for el in l2:
    el=el.split()
    if l.count(el[0])==1 and len(el[1]) in range(2,4) and el[2].isupper()==True and len(el[2])==3 and el[2].isalpha()==True and el[1].isdigit()==True:
        print(' '.join(el))

    

