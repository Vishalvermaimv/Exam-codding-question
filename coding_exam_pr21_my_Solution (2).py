arr=[[75, 76, 65, 87, 87],
     [78, 76, 68, 56, 89],
     [67, 87, 78, 77, 65]]
def main(arr,m,n):
    arr = []
    for i in range(m):
        row = [] # creating rows for number of students
        for j in range(n):
            ele = int(input(f'enter marks for student[{m+1}] for subject[{n+1}'))
            row.append(ele) #appending marks for each student
        arr.append(row)     #appending marks list to the array

# 
    l = list(map(list,zip(*arr)))
    sub_marks = [] #creating nested list for each subject
    for i in l:
        sub_marks.append(i) 
    print(sub_marks)
    avg_list=[]    #creating list for avg marks
    for i in sub_marks:
        avg=sum(i)/len(i)
        avg_list.append(avg) #appending avg marks to avg_list
    print(avg_list)
    min=avg_list[0]         #initialising min value
    for i in range(len(avg_list)): 
        if avg_list[i]<min: #checking min value with elements in avg_list
            min=avg_list[i]  #assigning min avg_value
    for i in sub_marks:
        if min==sum(i)/len(arr): #checking if min value equals with elements of sub_marks 
            sub_marks.remove(i)  #removing value after checking
    print(sub_marks)

    for i in zip(*sub_marks):
        print(sum(i),end=' ') #printing sum of remaining subject marks after deducting one subject marks


arr=[]
m = int(input('enter number of students'))
n = int(input('enter number of subjects'))
main(arr,m,n)