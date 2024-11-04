def run():
    # Pre-calculate the range to avoid repeated calculations
    range_10 = range(10)
    
    # Use a list comprehension for better performance
    hits = [str(i * j) for i in range_10 for j in range_10 if i > j]
    
    # Join the list directly without creating a temporary string
    print(','.join(hits))
    return