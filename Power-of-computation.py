# A poem about the power of computation

def poem(n):
    # The first line is always the longest
    if n == 0:
        return "The power of computation"
    else:
        return poem(n-1) + ", to solve problems"

print(poem(5))
