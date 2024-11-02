def my_function(n):
    """Performs a computationally intensive task."""
    # Use list comprehension for better performance
    return sum(i * i for i in range(n))

def run():
    """Main function to demonstrate latency profiling."""
    n = 10000000
    result = my_function(n)

def is_prime(n):
    # Optimize prime check by reducing the range and adding early exits
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True