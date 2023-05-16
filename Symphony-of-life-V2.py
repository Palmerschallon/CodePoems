# A whisper of zero and one
fib_sequence = [0, 1]

# In the quiet,
for i in range(2, 5):
    
    # Each number a secret
    fib_sequence.append(
        
        # Told by the two before
        fib_sequence[i - 1] + fib_sequence[i - 2]
    )
    
# The whispers grow
for number in fib_sequence:
    
    # Into a symphony of life
    print(number)
