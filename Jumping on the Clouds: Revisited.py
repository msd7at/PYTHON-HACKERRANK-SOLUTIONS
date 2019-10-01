n,k=map(int,input().split())
c=list(map(int,input().split()))
i=0
e=100
while 0<1:
    jp=(i+k)%n
    i=jp
    if c[i]==1:
        e=e-2-1
    else:
        e=e-1
    if i==0:
        break
print(e)
