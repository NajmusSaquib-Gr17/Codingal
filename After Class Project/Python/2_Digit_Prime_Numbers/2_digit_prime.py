def sieveOfEratosthenes(n):
    if n <= 2:
        return 0
    isPrime = [True] * (n+1)
    isPrime[0] = isPrime[1] = False

    p = 2
    while(p*p <= n):
        for notPrime in range(p*p, n+1, p):
            isPrime[notPrime] = False
        p += 1
    

    Primes = [notPrime for notPrime, Prime in enumerate(isPrime) if Prime]
    return Primes

n = 99   
primeNumber = sieveOfEratosthenes(n)
twoDigitPrime = [p for p in primeNumber if range(10, 99)]
print("Two Digit Prime Numbers from 10-99\n", twoDigitPrime)
            