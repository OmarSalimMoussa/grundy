import time

def some_function(n):
    """Performs a computationally intensive task with a string."""
    # Optimize string concatenation using list and join
    result = ['.']
    for _ in range(n):
        result.extend(result)
    return ''.join(result)

def fib(n):
    # Optimize fibonacci function using dynamic programming
    if n <= 1:
        return n
    fib_array = [0] * (n + 1)
    fib_array[1] = 1
    for i in range(2, n + 1):
        fib_array[i] = fib_array[i-1] + fib_array[i-2]
    return fib_array[n]

def run():
    """Main function to demonstrate profiling with string."""
    n = 14
    start_time = time.time()
    result = some_function(n)
    end_time = time.time()
    print('Result:', result)
    print('Elapsed time:', end_time - start_time, 'seconds')