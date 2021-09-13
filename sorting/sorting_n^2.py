'''
Proszę zaproponować algorytm, który w czasie liniowym sortuje tablicę 
zawierającą n liczb ze zbioru [0, n^2−1]. 
'''

def counting_sort(arr, ctr):
    n = len(arr)
    k = 10

    keys = [0]*k
    sorted = [0]*n

    for i in range(n):
        keys[(arr[i]//ctr)%10] += 1

    for i in range(1,k):
        keys[i] += keys[i-1]

    for i in range(n-1,-1,-1):
        sorted[keys[(arr[i]//ctr)%10]-1] = arr[i]
        keys[(arr[i]//ctr)%10] -= 1

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

