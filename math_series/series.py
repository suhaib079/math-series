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



def sum_series(n, v1=0, v2=1):
    if n == 0:
        return v1
    if n == 1: 
       return v2
    else:
        return sum_series(n-1,v1,v2) + sum_series(n-2,v1,v2)


print(fibonacci(8))
print(lucas(7))
   
 
 
