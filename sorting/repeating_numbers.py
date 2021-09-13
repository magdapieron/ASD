'''
Dane są dwie tablice typu int t[max]. W każdej z tablic znajdują się niepowtarzające się,
uporządkowane  rosnąco liczby naturalne. Napisać efektywną funkcję zwracającą liczbę 
elementów występujących w obu  tablicach równocześnie.  

***

Wychodzi O(2*max) w najgorszym przypadku 

'''

def find_repeating(arr1, arr2):
    max = len(arr1)
    i = j = ctr = 0
    while(i < max and j < max):
        if(arr1[i] > arr2[j]):
             j += 1
        elif(arr1[i] < arr2[j]):
            i += 1
        else:
            ctr += 1 
            j += 1 
            i += 1
    return ctr



arr1 = [1,2,4,7,10,18,21,22,23,24]
arr2 = [1,3,5,7,8,9,11,15,21,22]
print(find_repeating(arr1,arr2))