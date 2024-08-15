def merge(arr, p, q, r):
    
    left_arr_len = q-p+1
    right_arr_len = r-q
    
    left_temp = []
    right_temp = []
    
    for i in range(left_arr_len):
        left_temp.append(arr[i+p])
        
    for i in range(right_arr_len):
        right_temp.append(arr[i+q+1])
        
    left_temp.append(float('inf'))
    right_temp.append(float('inf'))
        
    left_index = 0
    right_index = 0
    
    for i in range(p,r+1):
        if(left_temp[left_index] <= right_temp[right_index]):
            arr[i] = left_temp[left_index]
            left_index = left_index + 1
        else:
            arr[i] = right_temp[right_index]
            right_index = right_index + 1
            
    return arr
        
def mergesort(arr,p,r):
    q = (r+p)//2
    if (p < r):
        arr = mergesort(arr,p,q)
        arr = mergesort(arr,q+1,r)
        return merge(arr,p,q,r)
    else:
        return arr