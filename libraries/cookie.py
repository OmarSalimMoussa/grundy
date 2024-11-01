import time

def some_function(n):
    """Performs a computationally intensive task with a string."""
    # Use string multiplication instead of iterative concatenation
    # This is more efficient for large strings
    return '.' * (2**n - 1)

def fib(n):
    # Use dynamic programming to optimize Fibonacci calculation
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
    fib_result = fib(15)  # Calculate Fibonacci number
    end_time = time.time()
    print('Fibonacci result:', fib_result)
    print('Result:', result)
    print('Elapsed time:', end_time - start_time, 'seconds')