
def nearst_smallest(arr):
    res = []
    for i in range(len(arr)):
        for j in range(1,i+1):
            if arr[i-j] < arr[i]:
                res.append(arr[i-j])
                break
        else:
            res.append(-1)
    print(res)
    

def nearest_Smalest_optimized(arr):
    stack = []
    res = []
    for i in range(len(arr)):
        if len(stack) < 1:
            res.append(-1)
            stack.append(arr[i])
        else:
            cur = len(stack)-1
            while len(stack) > 0:
                if stack[cur] < arr[i]:
                    res.append(stack[cur])
                    stack.append(arr[i])
                    break
                else:
                    stack.pop(cur)
                cur -= 1
    print(res)


arr = [4,10,5,8,20,15,3,12]
nearest_Smalest_optimized(arr)