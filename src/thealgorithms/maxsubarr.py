def find_max_cross_subarr(arr,low,mid,high):
    left_sum = float('-inf')
    sum = 0
    max_left = mid
    for i in range(mid,low-1,-1):
        sum = sum + arr[i]
        if (sum > left_sum):
            left_sum = sum
            max_left = i
    right_sum = float('-inf')
    sum = 0
    max_right = mid+1
    for i in range(mid+1,high+1):
        sum = sum + arr[i]
        if (sum > right_sum):
            right_sum = sum
            max_right = i
            
    return max_left, max_right, (left_sum+right_sum)