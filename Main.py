n = int(input("Enter the Range for the Array:"))
arr = []
for i in range(n):
    arr.append(int(input()))

search = int(input("Enter the search element in the array:"))
flag = False
pos = 0
for i in range(len(arr)):
    if(search == arr[i]):
        pos = i
        flag = True
        break

if(flag == True):
    print("The Element is present in the Array index at" , pos , "And the Element is :" , arr[pos])
else:
    print("Element is not present in the array")


def binarySearch(arr, low , high , x):
    if(high >= low):

        mid = (high + low)//2

        if arr[mid] == x:
            return mid
        
        elif arr[mid] >  x:
            return binarySearch(arr , low , mid - 1 , x)
        else:
            return binarySearch(arr , mid + 1 , high , x)
    
    else:
        return 0

n = int(input("Enter the Range for the Array:"))
arr = []
for i in range(n):
    arr.append(int(input()))

search = int(input("Enter the search element in the array:"))

result = binarySearch(arr , 0 , len(arr) - 1, search)
if(result != 0):
    print("Element is present at the index at:" , result)
else:
    print("Element is not present at the array")


