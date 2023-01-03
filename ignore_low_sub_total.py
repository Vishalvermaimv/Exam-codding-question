
"""
N = students
M = subjects 

2d array []
students x subjects marks

eg 
3   3
50 30 70
30 70 99
99 20 30

return total for each by ignore low avg subject.
eg 120 129 129
"""


def calc_total(n, m, arr):
    avg = [] 
    total = []
    ridx = None
    small = None
    for count, data in enumerate(arr):
        print("student", count, " = ", data)
        total.append(sum(data))
        for count_sub, data1 in enumerate(data):
            #  print("#### indx", count_sub)
              if len(avg)>count_sub:
                  avg[count_sub]=avg[count_sub]+data1
              else:
                  avg.insert(count_sub, data1) 
    for i in avg:
        i_tmp = i//30
        if not small or small >i_tmp:
            small =i_tmp
            ridx= avg.index(i)
   # print("### old total", total)
    for ix, i in enumerate(total) :
       # print("###minus", total[ix], arr[ix][ridx]) 
        total[ix] = total[ix] - arr[ix][ridx]
    #print(">>> sub avg", avg, total, ridx, small)
    return " ".join(list(map(str, total))) 
   

n, m = 0,0
inp_ = input(" n m = ")
if inp_:
    n, m = map(int, inp_. split())
print("## n m =", n, m)

arr = []
#arr = [[50,30,70], [30,70,99], [99,20, 30]]

for i in range(n):
        inp_1 = input(f" marks  for student {i}, subject {m} = ")
        inp2 = inp_1.split()
        if inp_1 and len(inp2)==m :
            arr.append(list(map(int, inp2))) 
          
if len(arr)==n :
   print(" return =",calc_total(n, m, arr))

 

