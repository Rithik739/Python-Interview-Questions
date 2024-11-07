def max_min(arr):
    if len(arr)==0:
        return None, None
    else:
        max = arr[0]
        min = arr[0]

        for i in arr:
            if i>max:
                max=i
            if i<min:
                min=i
        return max, min
    
arr = [1,8,92,0,-1]
a,b=max_min(arr)
print("max value", a)
print("min value", b)