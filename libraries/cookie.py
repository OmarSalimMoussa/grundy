import time

def some_function(n):
    """Performs a computationally intensive task with a string."""
    # Optimization: Use string multiplication instead of concatenation in a loop
    # This reduces the number of string allocations and copies
    return '.' * (2**n - 1)

def fib(n):
    # Optimization: Use dynamic programming to calculate Fibonacci numbers
    # This reduces time complexity from O(2^n) to O(n)
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def run():
    """Main function to demonstrate profiling with string."""
    n = 14
    start_time = time.time()
    result = some_function(n)
    end_time = time.time()
    print('Result:', result)
    print('Elapsed time:', end_time - start_time, 'seconds')