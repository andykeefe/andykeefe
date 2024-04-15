![main-image](https://github.com/andykeefe/andykeefe/assets/154836099/6dfaab0f-5988-4563-a4e1-f86161f31ee8)


_Perspectival Drawing with Three Cubes_ by Peter Flötner, 1528


Block Cipher Cryptography
--------------------------------------------------------------------------------------------
This section covers cryptography most commonly used in the web: block ciphers. Block ciphers encrypt each block of plaintext with the same key. The length of the block depends on the cipher. For example, AES uses 128 bit length blocks, while DES uses 64 bit length blocks. 

Block ciphers are excellent for providing diffusion. On average, one change in plaintext bit results in the change of half of the output bits (Paar and Pelzl, 2010, p. 58). 

![image](https://github.com/andykeefe/andykeefe/assets/154836099/0c8d1475-36f8-4915-8121-9de7d2fb5569)

Block ciphers can be used in some hash functions. For example, the Davies-Meyer hash constructions use block cipher techniques. _e_ represents a block cipher in the expression below.

![image](https://github.com/andykeefe/andykeefe/assets/154836099/5c5097d0-defb-411a-ac74-aa32f22d187e)


