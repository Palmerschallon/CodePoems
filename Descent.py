def factorial(n):
    # Climbing the steps
    if n == 0:
        # We reach the top
        return 1
    else:
        # One step at a time
        return n * factorial(n-1)
        
# The descent, just as important
print(factorial(5))
