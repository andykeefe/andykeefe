![main-image](https://github.com/andykeefe/andykeefe/assets/154836099/b4e27e08-8ad6-48d0-ab82-a90deae91386)

Building a Catafalque, Tomb of Ipuy, 1279 BCE-1213 BCE

# Basics and symmetric cryptography


The authors call this a qualifying set. It gets you ready to write and think like a cryptographer. It requires a level of knowledge beyond just introductory coding, and it's definitely necessary to have open documentation for Python while doing it.

This set covers XOR operations and introduces the most widely used symmetric cryptographic scheme, the Advanced Encryption Standard (AES). We'll start by introducing the concepts behind symmetric cryptography, including its history and conventional operations, and then we'll briefly cover what the XOR operation does to bits. 

## Symmetric cryptography

Cryptography has been around for thousands of years. The first documented, surviving example of cryptography comes from Ancient Egypt, 1900 BCE, but didn't seem to be used for secretive communication as much as to glorify the death of a noblement. One of the most well-known and widely used example of cryptographic communication comes from Julius Caesar [1]. You may know of him from his crossing of the Rubicon or that time he got stabbed a bunch. The cipher he used (appropriately referred to as a 'Caesar Cipher') used a numerical value to shift and substitute the plaintext message. For example, assume our plaintext message is "ITHINKIWILLCONQUERGAUL" and our key is 3. Each letter would then be shifted and substituted by the letter 3 characters from it. 'I' becomes 'L', 'T' becomes 'W', 'H' becomes 'K', and so on. So our original message 

ITHINKIWILLCONQUERGAUL

is encrypted to

LWKLQNLZLOOFRQTXHUJDXO

To decrypt the ciphered message, the recipient would need to have knowledge of the key. Notice that the encryption and decryption key are of the same value, just with "reversed" operation. This is the concept of _symmetric keys_, and the backbone of today's symmetric cryptography: to decrypt an encrypted message, both parties must share the same key.

It must be noted that _every_ historical cipher before 1960 used symmetric keys; for nearly 3000 years, symmetric key cryptography was the only way to go [2]. 

[1] Sidhpurwala, H. (2023, January 12). A Brief History of Cryptography. Red Hat Blog. https://www.redhat.com/en/blog/brief-history-cryptography 

[2] Smart, N. (2008). _Cryptography: An Introduction_. https://www.cs.umd.edu/~waa/414-F11/IntroToCrypto.pdf

# Exercises for set 1

1. Convert hex to base64
2. Fixed XOR
3. Single-byte XOR cipher
4. Detect single character XOR
5. Implementing repeating key XOR
6. Break repeating key XOR
7. AES in ECB mode
8. Detect AES in ECB mode
