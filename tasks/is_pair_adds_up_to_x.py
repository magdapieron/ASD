'''
Dana jest tablica zawierająca liczby naturalne. Proszę zaimplementować funkcję find_pair(arr, x) 
odpowiadającą na pytanie czy w tablicy jest para sumująca się do jakiejś liczby x. 
Funkcja powinna być jak najszybsza.
'''

def merge_sort(arr):

    n = len(arr)
    if(n > 1):
        middle = n//2
        left = arr[:middle]
        right = arr[middle:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while(i < len(left) and j < len(right)):
            if(left[i] < right[j]):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while(i < len(left)):
            arr[k] = left[i]
            i += 1
            k += 1

        while(j < len(right)):
            arr[k] = right[j]
            j += 1
            k += 1



def find_pair(arr, x):

    merge_sort(arr)


    if(arr[0] > x or x == 0):
        return False
    
    left = 0
    right = len(arr)-1
    
    while(left <= right):
        if(arr[left] + arr[right] < x):
            left += 1
        elif(arr[left] + arr[right] > x):
            right -= 1
        else:
            return True

    return False


arr = [1,4,2,7,16,10,2,25]
print(find_pair(arr,18))


