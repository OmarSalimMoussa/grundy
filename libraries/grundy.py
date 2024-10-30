def my_function(n):
    """Performs a computationally intensive task."""
    result = 0
    for i in range(n):
        result += i * i
    return result

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


def run():
    """Main function to demonstrate profiling."""
    n = 10000000
    result = my_function(n)
    result += fib(15)
    print(result)