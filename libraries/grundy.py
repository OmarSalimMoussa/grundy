def my_function(n):
    """Performs a computationally intensive task."""
    result = 0
    for i in range(n):
        result += i * i
    return result

def run():
    """Main function to demonstrate latency profiling."""
    n = 10000000
    result = my_function(n)
