from random import randrange, getrandbits

"""     This program generates the semiprime or product n of two large prime numbers p and q.
    Each time an odd number is generated, the program passes a conditional statement: so long
    as is_prime is not True, it will continue to generate prime candidates.         """

def is_prime(n, k=128):

    if n == 2 or n == 3:
        return True

    if n <= 1 or n % 2 == 0:
        return False

    s = 0
    r = n - 1

    while r & 1 == 0:
        s += 1
        r //= 2

    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)

        if x != 1 and x!= n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            
            if x != n - 1:
                return False
            
    return True




"""     generate_prime_candidate() generates a random integer of
    1024 bits in length using the getrandbits function we imported.
    The line after utilize two bitwise operations, | and <<, to set
    the least significant bit and most significant bit to 1, which 
    ensures that the generated number is odd.       """


def generate_prime_candidate(length):

    p = getrandbits(length)

    p |=(1 << length - 1) | 1

    return p


"""     generate_prime_number() initializes p to 4 as a starting point
    for the function. A while loop is initiated that continues until p
    passes the is_prime primality test. 128 signifies the number of
    primality tests performed.       """

def generate_prime_number(length=1024):

    p = 4

    while not is_prime(p, 128):
        p = generate_prime_candidate(length)

    return p



def main():

    print("Generating semiprime n of two prime numbers p and q:")
    print ("n = pq")

    p = generate_prime_number()
    q = generate_prime_number()
    n = p*q

    print(p)
    print("")
    print(q)
    print("")
    print(n)
    print("")
    print("Digits in semiprime:", len(str(n)))



if __name__ =='__main__':
    main()


