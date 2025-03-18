arr = [ 2, 3, 4, 10, 40 ] 
x = 10


def binarySearch (arr, l, n, x):  
    if n >= l: 
        if n%2 !=0:
            mid = l + (n - l)/2
        else:
            mid=3/2+(n-1)/2
        if arr[mid] == x: 
            return mid 
          
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        else: 
            return binarySearch(arr, mid + 1, n, x) 
  
    else: 
        return 0
  
 

   
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != 0: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")