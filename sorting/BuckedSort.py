from InsertionSort import insertion_sort


def bucked_sort(arr, n):
    Max = max(arr)
    buckets = [[] for _ in range(n)]

    for i in arr:
        number = i/Max
        index = (int)((n-1)*number)
        buckets[index].append(i)

    for i in range(n):
        buckets[i] = insertion_sort(buckets[i])

    ctr = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            arr[ctr] = buckets[i][j]
            ctr +=1


array = [1,7,2,4,3,5,2,8,3]
print(array)
bucked_sort(array,3)
print(array)