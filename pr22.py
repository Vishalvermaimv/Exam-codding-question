# A simple program to find the largest subarray 
# with equal number of 0s and 1s 
  
# This function Prints the starting and ending 
# indexes of the largest subarray with equal  
# number of 0s and 1s. Also returns the size  
# of such subarray. 
def findSubArray(arr, n): 
  
    sum = 0
    maxsize = -1
  
    # Pick a starting point as i 
  
    for i in range(0, n-1): 
      
        sum = -1 if(arr[i] == 0) else 1
  
        # Consider all subarrays starting from i 
  
        for j in range(i + 1, n): 
          
            sum = sum + (-1) if (arr[j] == 0) else sum + 1
  
            # If this is a 0 sum subarray, then  
            # compare it with maximum size subarray 
            # calculated so far 
  
            if (sum == 0 and maxsize < j-i + 1): 
                  
                maxsize = j - i + 1
                startindex = i 
              
          
      
    if (maxsize == -1): 
        print("No such subarray"); 
    else: 
        print(startindex, "to", startindex + maxsize-1)
        print(maxsize) 
  
    return maxsize 
  
# Driver program to test above functions 
arr = [1,1,0,1] 
size = len(arr) 
findSubArray(arr, size) 
  
# This code is contributed by Smitha Dinesh Semwal 