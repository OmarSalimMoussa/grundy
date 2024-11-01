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


@profile
def run():
    """Main function to demonstrate latency profiling."""
    n = 10000000
    result = my_function(n)
    # Remove the is_prime check as it's not significantly impacting performance
    # and its result is not used