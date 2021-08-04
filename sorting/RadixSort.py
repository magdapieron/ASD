def counting_sort(arr, ctr):
    n = len(arr)
    max = 10

    keys = [0]*max
    sorted = [0]*n

    for i in range(n):
        key = (arr[i]//ctr)%10
        keys[key] += 1

    for i in range(1,max):
        keys[i] += keys[i-1]

    for i in range(n-1,-1,-1):
        key = (arr[i]//ctr)%10
        sorted[keys[key]-1] = arr[i]
        keys[key] -=1

    for i in range(n):
        arr[i] = sorted[i]


def radix_sort(arr):
    Max = max(arr)
    ctr = 1

    while(Max//ctr > 0):
        counting_sort(arr, ctr)
        ctr *= 10



array = [234,2,18,90,65,12]
print(array)
radix_sort(array)
print(array)
