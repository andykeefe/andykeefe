![default](https://github.com/andykeefe/andykeefe/assets/154836099/26dfbd98-e0fd-4acc-9f95-049a97328683)

_Ciphers and Constellations in Love with a Woman_ by Joan Miró, 1941


Block and Stream Cryptography
-----------------------------
More block ciphers! Aren't you overjoyed?

This set focuses a bit more on CTR mode, which uses a block cipher as a stream cipher. The block cipher takes in a unique counter value each time, for example, an increasing counter as a new block is computed, and an initialization vector that stays the same. It is important to avoid using the same counter more than once. Therefore, CTR mode is theoretically very secure but relies on precise implementation. 

![image](https://github.com/andykeefe/andykeefe/assets/154836099/27c50f8b-8262-4d62-b69a-19a897cb8f66)


The last four exercises of this set revolve around the MT19937 Mersenne Twister Pseudo-Random Number Generator (PRNG), based on Mersenne prime $`2^{19937} - 1`$, including implementation, cracking the seed, cloning from output, creating a stream cipher from it and breaking it.

A random number generator intends to randomly generate sequences from an initial seed value. The goal is to approximate a sequence of random looking numbers even though the function itself is deterministic. Cryptographically secure pseudo-random number generators (CSPRNGs) are supposed to be entirely unpredictiable and are unique to cryptographic applications, especially stream ciphers (Paar and Pelzl, 2010, p. 35-36). 
