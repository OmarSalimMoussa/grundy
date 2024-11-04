from libraries import cookie, grundy, slinky

def main():
    # Run cookie.run() and slinky.run() concurrently to improve overall latency
    import concurrent.futures
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        future_cookie = executor.submit(cookie.run)
        future_slinky = executor.submit(slinky.run)
        concurrent.futures.wait([future_cookie, future_slinky])
    
    # Run grundy.run() separately as it's the most time-consuming operation
    grundy.run()

if __name__ == '__main__':
    main()