'''
Napisz funkcję, która sortuje litery nazwiska metodą prostego wstawiania. 
'''

def sort(last_name):
    n = len(last_name)
    arr = [0]*n

    for i in range(n):
        arr[i] = last_name[i]

    for i in range(1,n):
        val = arr[i]
        j = i-1
        while(ord(val) < ord(arr[j]) and j >= 0):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = val

    last_name = ""

    for i in range(n):
        last_name += arr[i]

    return last_name

name = "pieron"
name = sort(name)
print(name)