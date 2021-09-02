'''
    Dana jest nieskończona tablica, gdzie pierwsze n pozycji zawiera posortowane liczby naturalne, 
    a reszta tablicy ma wartości None. Nie jest dana wartość n. Przedstaw algorytm, który dla danej 
    liczby naturalnej x znajdzie indeks w tablicy, pod którym znajduje się wartość x. Jeżeli nie ma 
    jej w tablicy, to należy zwrócić None.
'''

def search(arr, x):

    right = 1
    while(arr[right] is not None and arr[right] <= x):
        right *= 2

    left = 0

    while(left<=right):
        avg = (left+right)//2
        if(arr[avg] == x):
            return avg
        elif(arr[avg] < x):
            left = avg
        else:
            right = avg

    return None


arr = [1,2,4,5,5,7,8,9, None, None, None, None, None, None, None, None, None]
print(search(arr,9))