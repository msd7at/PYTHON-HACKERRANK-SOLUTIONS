j=int(input())
s=input()
l=['a','b','c','d']
n=[]
io=["!",'@','#','$','%','^','&',')','(','*','-','+']
for i in s:
    if i.isdigit()==True:
        if "a" not in n:
            n.append("a")
    elif i.isupper()==True:
        if "b" not in n:
            n.append("b")
    elif i.islower()==True:
        if "c" not in n:
            n.append("c")
    elif i in io:
        if 'd' not in n:
            n.append('d')
if j<=6:
    q=len(n)
    if q==4:
        print(6-j)
    elif q<4:
        a=4-q
        j=j+a
        if j>5:
            print(a)
        else:
            h=6-j
            print(a+h)

else:
    print(4-len(n))

                

