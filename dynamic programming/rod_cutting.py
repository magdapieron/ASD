'''
Firma kupuje długie stalowe pręty i tnie je na kawałki, które sprzedaje. Kawałki mają długość w metrach
wyrażoną zawsze liczbą naturalną. Dla kawałka długości n metrów znane są ceny kawałków długości 1, 2, …, n
metrów. Firma chce znać maksymalny zysk, który może uzyskać z pocięcia i sprzedania pręta długości n.
'''

def cut_rod(n, price):      #price[i] to cena kawalka o dlugosci i
    max_price = [0]*(n+1)
    max_price[1] = price[1]

    for i in range(2,n+1):
        for j in range(1,i+1):
            max_price[i] = max(price[j]+max_price[i-j], max_price[i])

    print(max_price)
    return max_price[n]



price = [0,1,5,8,9,10,17]
print(cut_rod(4,price))
