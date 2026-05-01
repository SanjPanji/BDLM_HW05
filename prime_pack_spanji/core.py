import random
from typing import List


def is_prime(x: int) -> bool:
    """Check if x is a prime number."""
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return False
    return True


def primes(count: int) -> List[int]:
    """Generate a list of the first `count` prime numbers in ascending order."""
    result = []
    candidate = 2
    while len(result) < count:
        if is_prime(candidate):
            result.append(candidate)
        candidate += 1
    return result


def checksum(x: List[int]) -> int:
    """Calculate checksum of a list of integers."""
    current = 0
    for value in x:
        current = ((current + value) * 113) % 10_000_007
    return current


def pipeline(count: int = 1000, seed: int = 100) -> int:
    """Generate primes, shuffle with given seed, compute and return checksum."""
    prime_list = primes(count)
    random.seed(seed)
    random.shuffle(prime_list)
    return checksum(prime_list)
