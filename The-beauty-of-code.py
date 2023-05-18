# A poem about the beauty of code

def poem(n):
    # The first line is always the longest
    if n == 0:
        return "A poem about the beauty of code"
    else:
        return poem(n-1) + ", and the power of computation"

print(poem(5))
