import time

def some_function(n):
    """Performs a computationally intensive task with a string."""
    # Using a list and join for more efficient string concatenation
    result = ['.']
    for _ in range(n):
        result.extend(result)
    return ''.join(result)

def run():
    """Main function to demonstrate profiling with string."""
    n = 14
    start_time = time.time()
    result = some_function(n)
    end_time = time.time()
    # Remove print statements to reduce latency
    # print('Result:', result)
    # print('Elapsed time:', end_time - start_time, 'seconds')
    return result, end_time - start_time