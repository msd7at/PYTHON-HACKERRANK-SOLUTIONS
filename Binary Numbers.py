x=str(bin(int(input())))
x=x[2:]
maxi=0
i=0
c=0
while i<(len(x)):
    if x[i]=="1":
        c=c+1
    else:
        c=0
    if c>maxi:
        maxi=c
    i+=1   
print(maxi)
    
