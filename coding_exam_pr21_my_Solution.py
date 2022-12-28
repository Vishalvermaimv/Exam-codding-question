arr=[[75, 76, 65, 87, 87],
     [78, 76, 68, 56, 89],
     [67, 87, 78, 77, 65]]
l = list(map(list,zip(*arr)))
sub_marks = []
for i in l:
    sub_marks.append(i)
print(sub_marks)
avg_list=[]
for i in sub_marks:
    avg=sum(i)/len(i)
    avg_list.append(avg)
print(avg_list)
min=avg_list[0]
for i in range(len(avg_list)):
    if avg_list[i]<min:
        min=avg_list[i]
for i in sub_marks:
    if min==sum(i)/len(arr):
        sub_marks.remove(i)
print(sub_marks)

for i in zip(*sub_marks):
    print(sum(i),end=' ')


arr=[[75, 76, 65, 87, 87],
     [78, 76, 68, 56, 89],
     [67, 87, 78, 77, 65]]