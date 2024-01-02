""" The Miller-Rabin algorithm is a primality test. Miller's first test in 1976 was
    a deterministic algorithm, and Michael Rabin modified it to make it an 
    unconditional probablistic algorithm.

    A deterministic algorithm always produces the same output given a specific
    input, and are the most frequently studied types of algorithms in computer
    science. 
                """

import random


def power(x, y, p):

    res = 1
    x = x % p

    while (y > 0):

        if (y & 1):

            res = (res * x) % p

        y = y>>1

        x = (x * x) % p

    return res


def rabinMiller(d, n):

    """ 
        Pick a random number in [2, ... , n - 2] 
        and store it as variable a.             
                                                """

    a = 2 + random.randint(1, n - 4)


    """ Call the power function to find
           a^d % n                       """

    x = power(a, d, n)


    if (x == 1 or x == n - 1):
        return True


    while (d != n - 1):
        x = (x * x) % n
        d *= 2

        if (x == 1):
            return False
        if (x == n - 1):
            return True

    return False


def isPrime(n, k):

    # ----------------------- #
    # Check low primes first
    # ----------------------- #

    if (n <= 1 or n == 4):
        return False
    if (n <= 3):
        return True



    """ For the Miller-Rabin algorithm, we need to find an odd number
    such that n - 1 = 2^s * d, where s is the largest power of 2 that 
    devides n - 1.

        The code loops, repeatedly dividing d by 2 until it is odd. 
    Since d = 99,999, I don't think this loop occurs.                   """

    d = n - 1
    while (d % 2 == 0):
        d //= 2
    

    """ The k variable specifies the amount of times the program iterates through
    the possible primes. This is specified in the main() function.                  """

    for i in range(k):
        if (rabinMiller(d, n) == False):
            return False

    return True


def main():
    
    k = 4  # Number of times the program will iterate. Higher k = greater accuracy

    print("Primes smaller than 100000: ")
    print()

    for n in range(1, 100000):
        if (isPrime(n, k)):      # Call isPrime function
            
            print(n, end="--")

    print('\n' * 2)



if __name__ == '__main__':
    main()





