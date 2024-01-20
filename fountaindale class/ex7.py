"""  This exercise is adapted from the book "Implementing Cryptography with Python"
    by Shannon Bray, chapter 3, page 68. They differ in that this program 
    allows the program user to input a password repeatedly rather than having
    it fixed. It also uses randomized rather than a fixed salt                 """

import hashlib
import os
import time

def saltPasswd_sha512(password):
    
    salt = os.urandom(32)
    print("      Salt: %s" % salt)
    print("      Value to be hashed: %s\n" % (password + salt))
    
    hash_value = hashlib.sha512(password + salt).hexdigest()
    print("      The length of the password: %s" % len(password))
    print("      Length of hash: %s\n" % len(hash_value))
    print("      Length of hash in bits: %s" % (len(hash_value) * 4)))
    return(hash_value)


def main():
    while True:
        
        print("Choose a password: ")
        plaintext = input()

        pass_bytes = bytes(plaintext, 'UTF-8')
        hashed_passwd = saltPasswd_sha512(pass_bytes)
        print("Hash digest to be stored: %s\n\n" % hashed_passwd)
        time.sleep(1)


if __name__ == '__main__':
    main()
