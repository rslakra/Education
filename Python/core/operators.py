# Arithmetic Operations

# sum all the values
def sum(*args):
    print(f"args: {args}")
    sum = 0
    for arg in args:
        sum += arg

    return sum

print()
print("Sum of (2 + 3):")
print(sum(2,3))

print(f"Sum of ({2,3,4,5}):")
print(sum(2,3,4,5))
print()