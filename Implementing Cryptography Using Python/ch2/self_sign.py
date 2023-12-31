"""

This code generates a self-signed certificate. Don't trust a certificate
that is signed by the entity you're trying to certify. The issuer and the 
signer of the certificate are the same.

"""

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
import datetime


encrypt_pass = b"iNeeds0up"

key = rsa.generate_private_key(public_exponent=65537, key_size=2048,
        backend=default_backend())

with open("rsakey.pem", "wb") as f:
    f.write(key.private_bytes(encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(encrypt_pass), ))


subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"IL"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"Chicago"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Keefe Industries"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"andy.us"), ])

cert = x509.CertificateBuilder().subject_name(subject).issuer_name(issuer
        ).public_key(key.public_key()
        ).serial_number(x509.random_serial_number()
        ).not_valid_before(datetime.datetime.utcnow()
        ).not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=10)
        ).add_extension(x509.SubjectAlternativeName([x509.DNSName(u"localhost")]),

critical=False,
    ).sign(key, hashes.SHA256(), default_backend())

with open("certificate.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))
