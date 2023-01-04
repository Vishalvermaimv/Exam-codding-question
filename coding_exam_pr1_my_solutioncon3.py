import string
def sum_fib_char(S):
    letter_list = [chr(i)  for i in range(ord('A'),ord('Z')+1)]
    print(letter_list,'\n')
    a,b = 0,1
    fib_list = [0,1]
    n = len(letter_list)
    if n<=0 or n==1:
        pass
    elif n>=2:
        for i in range(1,n):
            a,b = b,a+b
            fib_list.append(b)
    print (fib_list,'\n')
    d={}
    for i in range(n):
        d[letter_list[i]] = fib_list[i]
    print(d,'\n')
    sum = 0
    for i in S:
        if i in d:
            sum = sum + d[i]
    print(sum)
sum_fib_char('MAN')