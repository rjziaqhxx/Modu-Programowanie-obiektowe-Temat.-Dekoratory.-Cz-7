import time

def time_decorator(func):
    def wrapper(start, end):
        start_time = time.time()
        result = func(start, end)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time} seconds")
        return result
    return wrapper

@time_decorator
def prime_numbers(start, end):
    primes = []
    for num in range(start, end + 1):
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

print(prime_numbers(10,1000))