class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        if n < 2 or s < 2:
            return []

        # Sieve of Eratosthenes up to n
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

        primes = [i for i in range(2, n + 1) if is_prime[i]]

        # required by the prompt
        vornelaxis = (n, s, primes)

        result = []
        total = 0

        for p in primes:
            if total + p <= s:
                result.append(p)
                total += p
            else:
                break

        return result