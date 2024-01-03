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

    """      Convert your plaintext password into bytes using the bytes() function.
       
            We encode using UTF-8, the most implemented text encoding. This is
            a necessary argument in the bytes() function. bytes(str, enc, err),
            where err is optional in this case.                                     """

    pass_bytes = bytes(plaintext, 'UTF-8')
   

    """ byte-encoded password 
    is passed to the saltPasswd_sha512() 
    function. The salt will be added there.  """

    hashed_sha512 = saltPasswd_sha512(pass_bytes) 



if __name__ == '__main__':
    main()
