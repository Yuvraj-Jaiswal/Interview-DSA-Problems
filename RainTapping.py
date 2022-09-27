
def raincount(arr):
    left = [0 for _ in range(len(arr))]
    right = [0 for _ in range(len(arr))]
    left[0] = arr[0]
    right[len(arr)-1] = arr[len(arr)-1]
    water_unit = 0

    for i in range(1,len(arr)):
        left[i] = max(arr[i],left[i-1])

    for i in range(1,len(arr)):
        right[len(arr)-1-i] = max(arr[len(arr)-1-i],right[len(arr)-1-i+1])

    for i in range(len(arr)):
        water_unit += min(left[i],right[i]) - arr[i]

    return water_unit

print(raincount([3,1,2,4,0,1,3,2]))
