def simpson_integration(f, upper, lowwer, length):
    dx = (upper - lowwer) / length
    h1=dx / 3.0
    x=lowwer
    y=f(x)
    intergrationSum=y
    intergrationSum=intergrationSum*h1
    intergrationValue=[]
    intergrationValue[0]=intergrationSum
    for i in range(1, length):
        
    
    