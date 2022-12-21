def find_subquery_length(arr,n):
    s=0
    ml=0

    for start in range(n):
        sum = -1 if(arr[start])==0 else 1

        for end in range(start+1,n):
            sum= sum-1 if (arr[end]) == 0 else sum+1

            if sum==0 and ml<end-start+1:
                ml = end-start+1
                si=start

    if ml==0:
        print('no sub_array found')
        print(ml)
    else:
        print(si,'to',ml+si-1)
        print(ml)
arr=[1,0,1,0,1,1]
n=len(arr)
find_subquery_length(arr,n)


