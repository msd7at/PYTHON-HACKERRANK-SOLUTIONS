def twoStrings(s1, s2):
    d={}
    for i in s1:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in s2:
        if i in d:
            return 'YES'
    return "NO"
