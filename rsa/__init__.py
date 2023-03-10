from key import newkeys, PrivateKey, PublicKey
from pkcs1 import (
    encrypt,
    decrypt,
    sign,
    verify,
    DecryptionError,
    VerificationError,
    find_signature_hash,
    sign_hash,
    compute_hash,
)

# main1 to encrypt, decrypt and sign a file


def main1():
    ################## Key generation ##################
    print('################## Key generation ##################')

    # generate a keypair
    (pubkey, privkey) = newkeys(1024)

    # log the public  and private keys
    print("pubkey: %s %s" % (pubkey.n, pubkey.e))
    print("privkey: %s %s" % (privkey.n, privkey.d))

    ################## Encryption ##################
    print('################## Encryption ##################')

    # we will use the public key to encrypt target_file.txt, and the private key to decrypt it
    # the block size is 128 bytes, so we will read the file in 128 byte chunks
    # and encrypt each chunk separately
    with open("target_file.txt", "rb") as f:
        plaintext = f.read()
        # split the file into chunks of 128 bytes
        chunks = [plaintext[i: i + 117] for i in range(0, len(plaintext), 117)]
        # encrypt each chunk
        ciphertext = b"".join(encrypt(chunk, pubkey) for chunk in chunks)

    with open("target_file.txt.enc", "wb") as f:
        f.write(ciphertext)

    ################## Decryption ##################
    print('################## Decryption ##################')

    # we will use the private key to decrypt target_file.txt.enc, and the public key to verify it
    # the block size is 128 bytes, so we will read the file in 128 byte chunks
    # and decrypt each chunk separately

    with open("target_file.txt.enc", "rb") as f:
        ciphertext = f.read()
        # split the file into chunks of 128 bytes
        chunks = [ciphertext[i: i + 128]
                  for i in range(0, len(ciphertext), 128)]
        # decrypt each chunk
        plaintext = b"".join(decrypt(chunk, privkey) for chunk in chunks)

    with open("target_file.txt.dec", "wb") as f:
        f.write(plaintext)

    ################## Signing ##################
    print('################## Signing ##################')

    # sign target_file.txt
    with open("target_file.txt", "rb") as f:
        message = f.read()
    signature = sign(message, privkey, "SHA-256")
    with open("target_file.txt.sig", "wb") as f:
        f.write(signature)

    # verify target_file.txt.sig
    with open("target_file.txt", "rb") as f:
        message = f.read()
    with open("target_file.txt.sig", "rb") as f:
        signature = f.read()
    try:
        verify(message, signature, pubkey)
        print("signature is valid")
    except VerificationError:
        print("signature is invalid")



# create a function that encrypt a file and take the path of the file as an argument
def encrypt_file(file_path, pubkey):
    # we will use the public key to encrypt target_file.txt, and the private key to decrypt it
    # the block size is 128 bytes, so we will read the file in 128 byte chunks
    # and encrypt each chunk separately
    with open(file_path, "rb") as f:
        plaintext = f.read()
        # split the file into chunks of 128 bytes
        chunks = [plaintext[i: i + 117] for i in range(0, len(plaintext), 117)]
        # encrypt each chunk
        ciphertext = b"".join(encrypt(chunk, pubkey) for chunk in chunks)

    with open(file_path + ".enc", "wb") as f:
        f.write(ciphertext)

# main2 to encrypt, decrypt and sign a folder of files


def main2():
    ################## Key generation ##################
    print('################## Key generation ##################')

    # generate a keypair
    (pubkey, privkey) = newkeys(1024)

    # log the public  and private keys
    print("pubkey: %s %s" % (pubkey.n, pubkey.e))
    print("privkey: %s %s" % (privkey.n, privkey.d))

    ################## Encryption ##################
    print('################## Encryption ##################')

    # get the path of the folder to encrypt
    folder_path = input("Enter the path of the folder to encrypt: ")

    #


if __name__ == "__main__":

    main1()

__all__ = [
    "newkeys",
    "encrypt",
    "decrypt",
    "sign",
    "verify",
    "PublicKey",
    "PrivateKey",
    "DecryptionError",
    "VerificationError",
    "find_signature_hash",
    "compute_hash",
    "sign_hash",
]
