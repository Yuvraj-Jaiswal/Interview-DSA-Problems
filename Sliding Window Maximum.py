
def max_sliding(arr,k):
    for i in range(0,len(arr)-k+1):
        greatest = arr[i]
        for j in range(i,i+k):
            if arr[j] > greatest:
                greatest = arr[j]
        print(greatest , end=" ")

max_sliding([4,1,3,5,1,2,3,2,1,1,5],3)
