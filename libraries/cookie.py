import time

def some_function(n):
    """Performs a computationally intensive task with a string."""
    result = '.'
    for i in range(n):
        result += result
    return result


def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def run():
    """Main function to demonstrate profiling with string."""
    n = 14
    start_time = time.time()
    result = some_function(n)
    end_time = time.time()
    print(fib(15))
    print('Result:', result)
    print('Elapsed time:', end_time - start_time, 'seconds')
