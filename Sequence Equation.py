n=int(input())
x=list(map(int,input().split()))
x.insert(0,0)
for i in range(1,n+1):
    y=x.index(i)
    print(x.index(y))
