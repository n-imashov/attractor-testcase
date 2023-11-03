class CesarCipher(object):
    _alphabet = "abcdefghijklmnopqrstuvwxyz"
    _shift = 3

    def set_alphabet(self, value):
        self._alphabet = value

    def set_shift(self, value):
        self._shift = value

    def encode(self, plainText):
        encoded_text = ""
        for char in plainText:
            if char in self._alphabet:
                char_index = self._alphabet.index(char)
                new_index = (char_index + self._shift) % len(self._alphabet)
                encoded_char = self._alphabet[new_index]
                encoded_text += encoded_char
            else:
                encoded_text += char
        return encoded_text


cesar_cipher = CesarCipher()
plain_text = "The quick brown fox jumps over the lazy dog"
encoded_text = cesar_cipher.encode(plain_text)
print(encoded_text)
