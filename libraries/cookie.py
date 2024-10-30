import time

def some_function(n):
    """Performs a computationally intensive task with a string."""
    result = '.'
    for i in range(n):
        result += result
    return result

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True


def run():
    """Main function to demonstrate profiling with string."""
    n = 14
    start_time = time.time()
    result = some_function(n)
    end_time = time.time()
    print('Result:', result)
    print('Is Prime: ', is_prime(10001011))
    print('Elapsed time:', end_time - start_time, 'seconds')
