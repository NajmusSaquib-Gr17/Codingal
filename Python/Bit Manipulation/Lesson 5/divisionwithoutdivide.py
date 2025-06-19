def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero.")    
    negative = (dividend < 0) != (divisor < 0)    
    dividend = abs(dividend)
    divisor = abs(divisor)
    quotient = 0
    for _ in range(dividend + 1):
        if dividend < divisor:
            break
        dividend -= divisor
        quotient += 1
    return -quotient if negative else quotient
print(divide(10, 3))    
print(divide(-15, 5))   
print(divide(20, -4))   
print(divide(-18, -6))  