def simpson_integration(f, upper, lowwer, length):
    dx = (upper - lowwer) / length
    h1=dx / 3.0
    x=lowwer
    y=f(x)
    intergrationSum=y
    intergrationSum=intergrationSum*h1
    intergrationValue=[]
    intergrationValue[0]=intergrationSum
    for index in range(1, length):
        tmp=index % 2
        x=index*dx+lowwer
        y=f(x)
        
        match tmp:
            case 0:
                intergrationSum=2*y
            case 1:
                intergrationSum=4*y
        intergrationSum=intergrationSum*h1
        
    x=upper
    y=f(x)
    intergrationSum=y
    intergrationSum            
    
        
    
    