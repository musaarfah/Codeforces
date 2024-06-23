def max_TV_money(x,y,prices):
    prices.sort()
    maxi=0
    for i in range(y):
        if prices[i]<=0:
            price=-prices[i]
            maxi+=price



    return maxi








x,y=map(int,input().strip().split())
prices=list(map(int,input().strip().split()))

print(max_TV_money(x,y,prices))
