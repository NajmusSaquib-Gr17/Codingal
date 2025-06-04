def sieve_of_eratosthenes(n):
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes


n = 1 #int(input("Enter the value of n: "))
prime_numbers = sieve_of_eratosthenes(n)
print(f"Prime numbers up to {n} are: {prime_numbers}")
