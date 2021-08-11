''' 
Proszę zaproponować algorytm, który mając dane dwa słowa o długości n, 
każde nad alfabetem  długości k, sprawdza czy są swoimi anagramami.
'''

def are_anagrams(str1, str2):
    if(len(str1) != len(str2)):
        return False

    n = len(str1)
    number_of_letters = (ord('z')-ord('a')+1)
    arr = [0]*number_of_letters

    for i in range(n):
        arr[ord(str1[i])-ord('a')] += 1
        arr[ord(str2[i])-ord('a')] -= 1

    for i in range(number_of_letters):
        if(arr[i] != 0):
            return False

    return True



print(are_anagrams("anagram", "maganra"))
print(are_anagrams("anagram", "maganraa"))