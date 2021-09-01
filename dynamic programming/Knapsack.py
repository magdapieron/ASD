def knapsack_sum(W,P,maxW):

    n = len(W)
   
    arr = [None]*n

    for i in range(n):
        arr[i] = [0]*(maxW+1)

    for i in range(W[0], maxW+1):
        arr[0][i] = P[0]

    for i in range(1,n):
        for j in range(1,maxW+1):
            arr[i][j] = arr[i-1][j]
            if(j >= W[i]):
                arr[i][j] = max(arr[i][j], arr[i-1][j-W[i]]+P[i])
    
    return arr[n-1][maxW]



P = [7,3,2,10,4,1,7,2]
W = [4,1,2,4,3,5,10,3]
print(knapsack_sum(W,P, 10))

    

