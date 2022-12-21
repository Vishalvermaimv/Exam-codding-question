arr=[1,0,1,1]
n=len(arr)
s=0

for i in range(n):
    c_0=0
    c_1=0
    for j in range(i,n):
        if arr[j]==0:
            c_0=c_0+1
        else:
            c_1=c_1+1
        if c_0==c_1:
            s=max(s,j-i+1)
print(s)
