def sum_of_alphabets(s):    
    a=0
    b=1
    arr={'A':0,'B':1}

    for i in range(ord('A'),ord('Z')):
        if chr(i) not in arr:
            a,b=b,a+b
            arr[chr(i)]=b
            
    sum=0
    for i in s:
        if i in arr:
            sum=sum+arr[i]
    print(sum)
s=input("Enter your String ").upper()
sum_of_alphabets(s)









