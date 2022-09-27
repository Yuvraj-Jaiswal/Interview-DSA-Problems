
arr = [1,2,2,1,3,1,1,3]
k = 4

def solve(arr,k):
    count = {}

    for i in range(k):
        if arr[i] in count:
            count[arr[i]] += 1
        else:
            count[arr[i]] = 1

    print(count.__len__())

    for i in range(0,len(arr)):
        if i+k < len(arr):

            if count[arr[i]] == 1:
                count.pop(arr[i])
            else:
                count[arr[i]] -= 1

            if arr[i+k] in count:
                count[arr[i + k]] += 1
            else:
                count[arr[i + k]] = 1

            print(count.__len__())


solve(arr,k)