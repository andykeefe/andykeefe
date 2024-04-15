![main-image](https://github.com/andykeefe/andykeefe/assets/154836099/3e402585-384e-4857-92a0-6e403ebb2a0b)

_Stamp Seal Inscribed for Amenhotep I_, New Kingdom, 1525-1504 BCE


Stream Cryptography and Randomness
------------------------------------------------

This set is the last focused on block cipher cryptography, and also covers message authentication codes. We've already covered block and stream ciphers, CTR and CBC mode, and a little about initialization vectors, so this write up will focus on authentication, MAC, and hashing algorithms.

Authentication is an easy concept to grasp. When you log into something, you need to enter a password or a biometric scan to verify that you are who you say are, when you use an ATM, you need to enter a PIN to access the account; when you try to trade a knock-off Babe Ruth baseball card from the 1930s, the auctioneer first verifies the authenticity (or lack, thereof) of the card. 

Message authentication codes (MACs) are one-way hash functions that provide integrity and authentication. Unlike other one-way functions, they are dependent on a key, specifically symmetric keys. Schneier notes the following: "An easy way to turn a one-way hash function into a MAC is to encrypt the hash value with a symmetric algorithm. Any MAC can be turned into a one-way hash function by making the key public" (Schneier, 2015, pp. 455-456).
