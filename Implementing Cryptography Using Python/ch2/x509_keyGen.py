"""

'cryptography' python library provides lots of modules and primitives
that make this a lot easier

"""

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes

"""
Generating the RSA private key
-------------------------------
Algorithm: RSA
Key length: 2048 bits
Public exponent = 65537
-------------------------------
"""

encryptedPass = b"iNeeds0up"
key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
        )

"""

Write generated key to rsakey.pem file 
Privacy Enhanced Mail (PEM): converts binary data into text format,
may be passed through communications channels.
Technically, this is a container format for certificate chains
including public and private keys and root certs, as well as public certs.

"""

with open("rsakey.pem", "wb") as f:
    f.write(key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(encryptedPass),
        ))

        """
        
        BestAvailableEncryption() just chooses the best algorithm available.
        In this case, likely AES-256, the current standard for security. We 
        use AES with the key Ilik32cod3 for encryption
        
        """

"""

CSR is created using CertificateSigningREquestBuilder() function, and is 
then signed using the private RSA key and a hash algorithm SHA-256. The CRS
contains information on country, state, name, org, and common name, as well
as an alternative DNS name

"""
csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"IL"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"Chicago"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Keefe Industries"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"andrewkeefe.us"),
    ])).add_extension(
            x509.SubjectAlternativeName([
                x509.DNSName(u"andrewkeefe.us"),
                ]),
            critical=False,
            ).sign(key, hashes.SHA256(), default_backend())


"""
Another PEM file created with the generated CSR written
to it.
"""

with open("csr.pem", "wb") as f:
    f.write(csr.public_bytes(serialization.Encoding.PEM))

    print('Operation complete.')
