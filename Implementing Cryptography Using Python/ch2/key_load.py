from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key


encrypted_pass = b'iNeeds0up'

key = load_pem_private_key(open('rsakey.pem', 'rb').read(), encrypted_pass, 
        default_backend())


csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([

    x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"IL"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"Chicago"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Keefe Industries"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"andy.org"),
    
    ])).add_extension(x509.SubjectAlternativeName([x509.DNSName(u"keefe.com"),]),
            critical=False,).sign(key, hashes.SHA256(), default_backend())

with open("csr.pem", "wb") as f:
        
    f.write(csr.public_bytes(serialization.Encoding.PEM))
