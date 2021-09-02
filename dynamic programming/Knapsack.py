def knapsack_sum(W,P,maxW):

    n = len(W)

    if(n == 0 or maxW == 0):
        return 0
   
    arr = [[0 for x in range(maxW + 1)] for x in range(n)]   # tworzę tablicę dwuwymiarową wypełnioną zerami
                                                             #f(i,0) = 0, f(0,maxW) = 0, gdy maxW<W[0]

    for i in range(W[0], maxW+1):      # dla n=0, od W[0] wpisujemy P[0], ze wzoru f(0, maxW) = P[0], gdy maxW>=W[0]
        arr[0][i] = P[0]

    for i in range(1,n):
        for j in range(1,maxW+1):
            arr[i][j] = arr[i-1][j]       
            if(j >= W[i]):          # jeśli kolejny element się mieści, to bierzemy ten bardziej opłacalny 
                arr[i][j] = max(arr[i][j], arr[i-1][j-W[i]]+P[i])
    
    val = arr[n-1][maxW]
    curVal = val
    curW = maxW
    indexes = []

    for i in range(n,0,-1):

        if curVal == arr[i - 1][curW]:
            if i - 1 == 0 and curVal != 0:
               indexes.append(0)

        elif curVal > 0:
            indexes.append(i)
            curVal -= P[i]
            curW -= W[i]

    return val, indexes



P = [7,3,2,10,3]
W = [4,1,2,4,5]
print(knapsack_sum(W,P, 8))

    

