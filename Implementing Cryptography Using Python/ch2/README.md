Chapter 2 covers perfect secrecy. This chapter is still a sort of intro into cryptography concepts.

In covering the basic principles of encryption and authentication, the first program you should look at is x509_keyGen.py.
X.509 certificates are the standard for public key certificates and are widely used in TLS/SSL internet protocols. The program 
generates two certificates, one an RSA-derived private key (rsakey.pem) that we will use to generate a public key, and the 
other a certificate signing request (csr.pem) that is signed with the private key. 

The next program to view is key_load.py, which serializes the private key and loads it to sign the CSR. If successful, the signed CSR 
can be viewed with an openssl command that can be seen in the csr.pdf file.

There's also a self-signed certificate, as in the issuer (or authenticator) of the cert is the same entity as the entity 
requesting certification, called self_sign.py. Don't trust an entity who certifies themselves.

The last program written is salt.py, which asks the user to input a password, converts it to bytes, hashes it using SHA-256 and some
salt, and outputs a hex digest. I might show this one to the class I am teaching. 
