""" This exercise is adapted from the book "Implementing Cryptography with Python"
    by Shannon Bray, chapter 3, page 68 """

import hashlib


def saltPasswd_sha512(password):
    
    salt = b'aRk4'
    print(password + salt)
    hash_value = hashlib.sha512(password + salt).hexdigest()

    """ The %s symbol passes a str variable into the function.
        In this context, salt value is printed, then a colon, and 
        finally the computed hexadecimal hash value.                """
    
    print("%s:%s" % (salt, hash_value))
    return hash_value


def main():
    while True:
        
        print("Choose a password: ")
        plaintext = input()

        pass_bytes = bytes(plaintext, 'UTF-8')

        hashed_sha512 = saltPasswd_sha512(pass_bytes) 


if __name__ == '__main__':
    main()
