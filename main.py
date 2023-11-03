class CesarCipher(object):
    _alphabet = "abcdefghijklmnopqrstuvwxyz"
    _shift = 3

    def set_alphabet(self, value):
        self._alphabet = value

    def set_shift(self, value):
        self._shift = value

    def encode(self, plainText):
        alphabet = self._alphabet
        shifted_alphabet = alphabet[self._shift:] + alphabet[:self._shift]
        translation = str.maketrans(alphabet, shifted_alphabet)
        return plainText.translate(translation)


cesar_cipher = CesarCipher()
plain_text = "The quick brown fox jumps over the lazy dog"
encoded_text = cesar_cipher.encode(plain_text)
print(encoded_text)
