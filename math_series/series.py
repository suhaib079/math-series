def fibonacci(n):
    if n <= 0:
        if n == 0:
            return 0
        else:
            return 1
    
    return fibonacci(n-1) + fibonacci(n-2)



def lucas(n):
    
    if n <= 1:
        if n == 0:
            return 2
        else:
            return 1

    return lucas(n-1) + lucas(n-2)

print(lucas(5))



def sum_series(n,x=0,y=1):
    
    if x == 2 and y == 1:
        return lucas(n)
    elif x == 0 and y == 1:
        return fibonacci(n)

    else:
        return fibonacci(n) + lucas(x)



print(fibonacci(8))
print(lucas(7))
   
 
 
