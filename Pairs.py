#link:-https://www.hackerrank.com/challenges/pairs/problem?h_l=interview&playlist_slugs%5B%5D=virtusa
def pairs(k, arr):
    d={}
    for i in arr:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    s=0
    for i in d:
        if i+k in d:
            s+=d[i+k]
    return s
