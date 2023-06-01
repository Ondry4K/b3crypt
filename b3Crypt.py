from cryptography.fernet import Fernet

class B3Crypt:
    def __init__(self, key=None):
        if key:
            self.key = key
        else:
            self.key = self.generate_key()

    @staticmethod
    def generate_key():
        return Fernet.generate_key()

    def encrypt(self, plaintext):
        f = Fernet(self.key)
        ciphertext = f.encrypt(plaintext.encode('utf-8'))
        return ciphertext

    def decrypt(self, ciphertext):
        f = Fernet(self.key)
        plaintext = f.decrypt(ciphertext)
        return plaintext.decode('utf-8')
