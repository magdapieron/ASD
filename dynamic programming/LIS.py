# longest increasing subsequence

def print_LIS(arr, parents, i):
    if(parents[i] >= 0):
        print_LIS(arr,parents, parents[i])
    print(arr[i])


def LIS(arr):
    n = len(arr)
    lis = [1]*n
    parents = [-1]*n

    for i in range(n):
        for j in range(i):
            if(arr[j] < arr[i] and lis[i] < lis[j]+1):
                lis[i] = lis[j]+1
                parents[i] = j

    Max = max(lis)
    idx = 0
    for i in range(n):
        if(lis[i] == Max):
            idx = i
    print("longest increasing subsequence: ")
    print_LIS(arr,parents, idx)
    print("length: ")
    return Max

arr = [3,1,5,7,2,4,9,3,17,3]
print(LIS(arr))