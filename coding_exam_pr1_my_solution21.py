arr = [[75, 76, 65, 87, 87],
       [78, 76, 68, 56, 89],
       [67, 87, 78, 77, 65]]
def sum_marks(arr,n,m):
    arr = [[0]* m for m in range(n)]
    for i in range(n):
        for j in range(m):
            ele = int(input(f"Enter marks for student [{i+1}] subject [{j+1}] : "))
            arr[i].append(ele)
    print(arr)
    l = list(map(list,zip(*arr)))  
    sub_list = [i for  i in l]
    # for i in list(map(list,zip(*arr))):
    #     sub_list.append(i)
    print(sub_list)
    avg_list = [sum(i)/len(i) for i in sub_list]
    print(avg_list)

    min = avg_list[0]
    for i in range(len(avg_list)):
        if avg_list[i]<min:
            min = avg_list[i]
    print(min)
    sub_list = [i for i in sub_list if not min==sum(i)/len(i)]
    print(sub_list)

    output = [print(sum(i),end=' ') for i in zip(*sub_list)]




arr = []
n = int(input("enter no. of students "))
m = int(input("enter no. of subjects "))
sum_marks(arr,n,m)