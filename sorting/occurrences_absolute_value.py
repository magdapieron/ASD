''' Proszę zaimplementować funkcję: 
    int count(arr);
    Funkcja ta przyjmuje na wejściu posortowaną tablicę n liczb całkowitych, w której mogą pojawiać się duplikaty.
    Funkcja powinna zliczać ilość wystąpień różnych wartości bezwzględnych elementów występujących w tej tablicy.

    Przykład:

    Wejście: {-1, -1, 0, 0, 1, 1, 1}
    Wyjście: 2

    Wejście: {1, 1, 1}
    Wyjście: 1
'''

def count(arr):
    
    ctr = len(arr)
    i = 0
    j = ctr-1

    while(i<j):

        while(i != j and arr[i] == arr[i+1]):
            i += 1
            ctr -= 1

        while(i != j and arr[j] == arr[j-1]):
            j -= 1
            ctr -= 1

        sum = arr[i] + arr[j]

        if(sum == 0):
            i += 1
            j -= 1
            ctr -= 1

        elif(sum < 0):
            i += 1

        else:
            j -= 1

    return ctr

        

arr = [-5,-4,-1,-1,0,1,4,5,5,7]
print(arr)
print(count(arr))