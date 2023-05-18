def linear_search(arr, x):
    for i in range(len(arr)):
        if x == arr[i]:
            return i
        
    return -1

def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

def interpolation_search(arr, x):
    start = 0
    end = len(arr) - 1

    while start <= end and x >= arr[start] and x <= arr[end]:
        pos = start + ((end-start) // (arr[end]-arr[start])) * (x - arr[start])

        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            start = pos + 1
        else:
            end = pos - 1

    return -1



