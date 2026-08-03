'''write program in python a function that returns a list of all
 prime numbers up to a given number n'''

def find_primes(n):
    """Returns a list of all prime numbers up to a given number n."""
    if n < 2:
        return []
    
    # Create a boolean array to track prime status
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
    
    # Loop through numbers to mark multiples as composite
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
                
    # Filter and return the list of prime numbers
    return [num for num, prime in enumerate(is_prime) if prime]

# Example usage:
print(find_primes(30))
# Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
