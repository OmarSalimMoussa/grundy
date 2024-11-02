def my_function(n):
    """Performs a computationally intensive task."""
    # Using sum() with a generator expression is more efficient than a loop
    return sum(i * i for i in range(n))

def run():
    """Main function to demonstrate latency profiling."""
    n = 10000000
    # Avoiding unnecessary variable assignment
    return my_function(n) + int(is_prime(10001011))

def is_prime(n):
    # Optimized primality test
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True