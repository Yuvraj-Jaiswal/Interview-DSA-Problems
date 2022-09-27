arr = [1,3,4,-1,20,-15,6,-8,3,2,-45]
find = 23

def subarray_sum_bruteforce(arr,k):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            sum_arr = 0

            for n in range(i,j+1):
                sum_arr += arr[n]

            if sum_arr == k:
                print([i,j])
                return [i,j]


def subarray_sum_half_optimization(arr,k):
    for i in range(len(arr)):
        sum_arr = 0
        for j in range(i+1,len(arr)):
            sum_arr += arr[j]

            if sum_arr == k:
                print([i+1,j])
                return


def subarray_sum_optimized(arr,k):
    sum_hash = {}
    sum_now = 0
    for i in range(len(arr)):
        sum_now += arr[i]

        if sum_now == k:
            print(0,i)
            return

        if sum_now-k in sum_hash:
            print(sum_hash[sum_now-k]+1,i)
            return

        else:
            sum_hash[sum_now] = i

subarray_sum_optimized(arr,find)