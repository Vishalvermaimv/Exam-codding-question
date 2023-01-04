def sum_of_alphabets(s):    
    a=0 #initialising 0
    b=1 #initialising1
    arr={'A':0,'B':1} #updating dictionary with 'A' and 'B'

    for i in range(ord('A'),ord('Z')+1): #for loop for checking if 'C' to 'Z' available or not
        if chr(i) not in arr: #if 'C' to 'Z' not available  
            a,b=b,a+b           #assign value of a to b as fibonacci number
            arr[chr(i)]=b       #update dictionary adding 'C' to 'Z' as key and fibonacci number as value
         
    sum=0                       #initialising sum
    for i in s:                 #loop on string variable 
        if i in arr.keys():            #if iterator available in dictionary
            sum=sum+arr[i]      #update sum
    print(arr)
    print(sum)
arr={'A':0, 'B':1}                  #printing sum for getting sum of  string characters
s=input("Enter your String ").upper()  #
sum_of_alphabets(s)                 #calling function to get the desired result









