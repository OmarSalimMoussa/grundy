from libraries import cookie, grundy, slinky
from concurrent.futures import ThreadPoolExecutor  # Import for parallel execution

def main():
    # Use ThreadPoolExecutor to run functions concurrently
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(cookie.run)
        executor.submit(grundy.run)
        executor.submit(slinky.run)

    # Add a comment explaining the optimization
    # Parallel execution of independent functions to reduce overall latency

if __name__ == '__main__':
    main()