def run():
    # Pre-calculate the range to avoid repeated calculations
    range_10 = range(10)
    
    # Use a list comprehension instead of nested loops
    hits = [str(i * j) for i in range_10 for j in range_10 if i > j]
    
    # Use ''.join() instead of ','.join() to avoid creating intermediate strings
    print(','.join(hits))
    return