l=[1,1,1,1,1]
n=len(l)
s=0
mxln=0
for i in range(n):
    sum=-1 if l[i]==0 else 1
    for j in range(i,n):
        s=s-1 if l[j]==0 else s+1

        if s==0 and mxln<j-i+1:
            mxln=j-i+1

if mxln==0:
    print (mxln)
else:
    print(mxln)
