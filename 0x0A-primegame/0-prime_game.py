#!/usr/bin/python3
"""
A solution to a prime number game
"""


def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def remove_multiples(nums, prime):
    """Removes multiples of a prime number from the list."""
    return [num for num in nums if num % prime != 0]


def isWinner(x, nums):
    """Determines the winner of the prime number game for multiple rounds."""
    if not nums or x < 1:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        nums_range = list(range(1, n + 1))
        maria_turn = True

        while True:
            prime = next((num for num in nums_range if is_prime(num)), None)
            if not prime:
                if maria_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            nums_range = remove_multiples(nums_range, prime)

            maria_turn = not maria_turn

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
