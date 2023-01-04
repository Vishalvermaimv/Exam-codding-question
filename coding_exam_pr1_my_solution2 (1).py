import string
def sum_of_letters (text):
    sum = 0
    letters =string.ascii_uppercase
    d = {'A':0, 'B':1}
    a=0
    b=1
    n=25
    print(d)
    print(letters)
    for letter in range(len(letters)):
        if letters[letter] not in d:
            a,b = b, a+b
            d[letters[letter]] = b
            
    print(d)
    for i in text:
        if i in d:
            sum = sum + d[i]
    return sum
print(sum_of_letters('MAN'))
