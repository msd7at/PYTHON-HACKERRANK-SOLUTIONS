ll=int(input())
ul=int(input())
l=[]
for i in range(ll,ul+1):
    if i==1:
        l.append(1)
    else:
        x2=i**2
        t=str(x2)
        ten=10
        qa=len(t)
        if qa%2==0:
            qa=int(qa/2)
        else:
            qa=int(qa/2)+1
        for j in range(qa):
            mod=x2%ten
            div=int(x2/ten)
            if mod!=0 and div!=0:
                c=div+mod
                if c==i:
                    l.append(i)
                    break
            ten=ten*10
if len(l)!=0:
    print(*l,end=' ')
else:
    print('INVALID RANGE')
