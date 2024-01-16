"""  This exercise is adapted from the book "Implementing Cryptography with Python"
    by Shannon Bray, chapter 3, page 68. They differ in that this program 
    allows the program user to input a password repeatedly rather than having
    it fixed.                                           """

import hashlib
import os


def saltPasswd_sha512(password):
    
    salt = os.urandom(8)
    print("Password: %s \nSalt: %s" % (password, salt))
    hash_value = hashlib.sha512(password + salt).hexdigest()

    """     The %s symbol passes a str variable into the function.
        In this context, salt value is printed, then a colon, and 
        finally the computed hexadecimal hash value.                """
    
    print("The salt is %s and the hash value is %s" % (salt, hash_value))
    print("")
    print("The length of the plain password is %s and the length of the hash value is %s" % (len(password), len(hash_value)))
    print("")
    
    return hash_value


def main():
    while True:
        
        print("Choose a password: ")
        plaintext = input()

        pass_bytes = bytes(plaintext, 'UTF-8')

        hashed_sha512 = saltPasswd_sha512(pass_bytes) 


if __name__ == '__main__':
    main()
