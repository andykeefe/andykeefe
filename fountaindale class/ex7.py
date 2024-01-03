import hashlib


def saltPasswd_sha512(password):
    
    salt = b'aRk4'
    print(salt + password)
    print("")
    hash_value = hashlib.sha512(salt + password).hexdigest()

    print("%s:%s" % (salt, hash_value))
    return hash_value


def main():

    print("Choose a password: ")
    plaintext = input()

    pass_bytes = bytes(plaintext, 'UTF-8')

    hashed_sha512 = saltPasswd_sha512(pass_bytes) 


if __name__ == '__main__':
    main()
