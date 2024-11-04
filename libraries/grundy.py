def my_function(n):
    """Performs a computationally intensive task."""
    # Using sum() with a generator expression is more efficient than a loop
    return sum(i * i for i in range(n))

def is_prime(n):
    # Optimize prime checking algorithm
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Only check odd numbers up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def run():
    """Main function to demonstrate latency profiling."""
    n = 10000000
    result = my_function(n)