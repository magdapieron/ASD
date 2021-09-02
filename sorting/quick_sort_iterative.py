# Algorytm QuickSort (do sortowania tablicy liczb) w sposób iteracyjny
# Wykorzystując własny stos.

def partition(arr, left, right):
    pivot = arr[right]
    i = left
    for j in range(left,right):
        if arr[j] <= pivot :           
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            
    arr[i], arr[right] = arr[right], arr[i]
    return i


def sort(arr, left, right):
    size = right-left+1
    stack = [0]*size    # tworzę stos
    top = -1            # top = -1 oznacza pusty stos
    top += 1            # wstawiam na stos left i right
    stack[top] = left
    top += 1
    stack[top] = right

    while top >=0:
        right = stack[top]
        top -= 1
        left = stack[top]
        top -= 1
        pivot = partition(arr,left,right)

        if pivot-1>left:
            top += 1
            stack[top] = left
            top += 1
            stack[top] = pivot-1

        if pivot<right:
            top += 1
            stack[top] = pivot
            top += 1
            stack[top] = right


def quick_sort(arr):
    sort(arr,0,len(arr)-1)

array = [1,7,2,4,3,5]
print(array)
quick_sort(array)
print(array)