import time

def some_function(n):
    """Performs a computationally intensive task with a string."""
    # Use string multiplication instead of repeated concatenation
    return '.' * (2**n - 1)

def run():
    """Main function to demonstrate profiling with string."""
    n = 14
    def fib(n):
        # Use dynamic programming to optimize Fibonacci calculation
        if n <= 1:
            return n
        fib_array = [0] * (n + 1)
        fib_array[1] = 1
        for i in range(2, n + 1):
            fib_array[i] = fib_array[i-1] + fib_array[i-2]
        return fib_array[n]
    start_time = time.time()
    result = some_function(n)
    end_time = time.time()
    print('Result:', result)
    print('Elapsed time:', end_time - start_time, 'seconds')