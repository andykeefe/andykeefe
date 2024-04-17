![Ulam_spiral,Prime_factors_spiral](https://github.com/andykeefe/andykeefe/assets/154836099/53478f87-74a5-4ad6-a3ee-274c9235940f)

_Ulam Spiral_ by Stanisław Ulam, 1964


Number Theoretic Cryptography
------------------------------------

The last four sets have dealt with symmetric cryptography, for example, block ciphers like AES, and MACs using symmetric keys. Symmetric cryptography has been the standard for thousands of years. Now we're getting into the newer, far more mathematical field of asymmetric cryptography, or public key cryptography. Public key algorithms rely on three types of computational problems:
1. Integer factorization: RSA is based on this, for example
2. Discrete logarithms in finite fields: Diffie-Hellman is based on this, for example
3. Elliptic curve schemes: Elliptic Curve Diffie Hellman (ECDH) is based on this, for example 

First, I'll talk about integer factorization. I'll assume that you know what a prime number is. You can google it if you don't. An interesting mathematical principle is that every number can be factored into a unique set of primes. This is the Fundamental Theorem of Arithmetic, first described in Euclid's _Elements_, stated by Kamal al-Din al-Fārisī, and formally proved by Gauss. 

Take these examples:

- $`54 = 3\times 3\times 3 \times 2 `$


- $`165 = 11 \times\ 3 \times\ 5 `$


- $`654,654,681 = 3 \times\ 3 \times\ 23 \times\ 47 \times\ 67289 `$


- $`4,654,879,854,656 = 2 \times\ 2 \times\ 2 \times\ 2 \times\ 2 \times\ 2 \times\ 5153 \times\ 14114593`$

Think about the increasing complexity of these examples; the larger the number, the more difficult it becomes to factor into unique primes. This is one of the core security principles of RSA, formalized in 1977 by Ron Rivest, Adi Shamir, and Leonard Adleman (but actually discovered a few years earlier by researchers at Britain's GCHQ), which is one of the algorithms covered in the latter half of this set. RSA will generate a product of two primes, a semi-prime $` n = pq `$, that is over 600 digits long; factoring this integer is currently too intensive to be computationally feasible. Quantum computing may change this in the future, but for now, quantum decoherence and costly quantum error-correction makes efficient cryptanalysis impractical for quantum computers.

RSA wasn't the birth of asymmetric/public-key cryptography. That would come a year earlier, in 1976, by Whitfield Diffie and Martin Hellman. Just kidding, the GCHQ, specifically James H. Ellis, formulated the concept of public key cryptography in 1969 but it was classified until 1997, after he died (Hoffstein, et al., 2008, p. 59). GCHQ was cooking, apparently. 

Anyway. Before getting into the discrete logarithm problem, let's look at how Diffie-Hellman key exchange is set up and operates. 

- First, choose a large prime _p_.
- Choose an integer α ∈ {2, 3, ..., _p_ - 2}.
- Publish _p_ and α

![image](https://github.com/andykeefe/andykeefe/assets/154836099/f21ea42e-8324-4df2-9483-eac5c0b601a0)

_k_ is the shared secret that will act as the session key between the two parties doing the key exchange.
Here's a better look at the sequence with which the key is exchanged:

![image](https://github.com/andykeefe/andykeefe/assets/154836099/eaa49610-d4d7-4c11-a7e4-9952248e7ad9)

(Paar and Pelzl, 2010, pp. 206-207)

To fully understand the discrete logarithm problem, it helps to have some background in abstract algebra, which I'm sure sounds really fun for you. I'll give some resources below for those willing to satiate their curiosity and fulfill their understanding as robustly as possible.

If you've studied calculus and some linear algebra, check out this free textbook:
- Beezer, R.A. (2015) _A First Course in Linear Algebra_
  - Part 1 (pp. 11-74) deals with Groups and Subgroups

If you want a quick mathematical overview:
- Hoffstein, J., et al. (2008). _An Introduction to Mathematical Cryptography_
  - pp. 72-75

If you want an overview of stuff only related to Diffie-Hellman:
- Paar, C., Pelzl, J. (2010). _Understanding Cryptography_
  - pp. 208-219
