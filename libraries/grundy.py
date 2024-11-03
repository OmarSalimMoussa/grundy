def my_function(n):
    """Performs a computationally intensive task."""
    # Use list comprehension for better performance
    return sum(i * i for i in range(n))

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Optimize by checking only up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def run():
    """Main function to demonstrate latency profiling."""
    n = 10000000
    result = my_function(n)