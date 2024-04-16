![Ulam_spiral,Prime_factors_spiral](https://github.com/andykeefe/andykeefe/assets/154836099/53478f87-74a5-4ad6-a3ee-274c9235940f)

_Ulam Spiral_ by Stanisław Ulam, 1964


Number Theoretic Cryptography
------------------------------------

The last four sets have dealt with symmetric cryptography, for example, block ciphers like AES, and MACs using symmetric keys. Symmetric cryptography has been the standard for thousands of years. Now we're getting into the newer, far more mathematical field of asymmetric cryptography, or public key cryptography. Public key algorithms rely on three types of computational problems:
1. Integer factorization: RSA is based on this, for example
2. Discrete logarithms in finite fields: Diffie-Hellman is based on this, for example
3. Elliptic curve schemes: Elliptic Curve Diffie Hellman (ECDH) is based on this, for example 

I'll assume that you know what a prime number is. You can google it if you don't. An interesting mathematical concept is that every number can be factored into a set of primes. 

Take these examples"

$`54 = 9 \times\ 6 = 3\times 3\times 3 \times 2 `$


$`165 = 33\times\ 5 = 11 \times\ 3 \times\ 5 `$


$`654,654,681 = 3 \times\ 3 \times\ 23 \times\ 47 \times\ 67289 `$


$`4,654,879,854,656 = 2 \times\ 2 \times\ 2 \times\ 2 \times\ 2 \times\ 2 \times\ 5153 \times\ 14114593`$

Think about the increasing complexity of these examples; the larger the number, the more difficult it becomes to factor into primes. This is one of the core security principles of RSA, which is one of the algorithms covered in this set. RSA will generate a product of two primes, a semi-prime $` n = pq `$, that is over 600 digits long; factoring this integer is computationally infeasible, so RSA is difficult, if not impossible, to crack. 



