def my_function(n):
    """Performs a computationally intensive task."""
    # Use a more efficient algorithm to calculate the sum of squares
    # This reduces the time complexity from O(n) to O(1)
    return (n * (n + 1) * (2 * n + 1)) // 6

def run():
    """Main function to demonstrate latency profiling."""
    n = 10000000
    result = my_function(n)

def is_prime(n):
    # Optimize prime checking algorithm
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