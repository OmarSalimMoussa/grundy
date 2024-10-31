def my_function(n):
    """Performs a computationally intensive task."""
    result = 0
    for i in range(n):
        result += i * i
    return result

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True

def run():
    """Main function to demonstrate latency profiling."""
    n = 10000000
    result = my_function(n)
    result += int(is_prime(10001011))
