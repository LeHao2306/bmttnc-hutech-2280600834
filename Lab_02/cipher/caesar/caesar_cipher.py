
from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, text: str, key: int) -> str:
        text = text.upper()
        encrypted_text = []
        for letter in text:
            if letter in self.alphabet:
                letter_index = self.alphabet.index(letter)
                output_index = (letter_index + key) % len(self.alphabet)
                output_letter = self.alphabet[output_index]
            else:
                output_letter = letter  # Không mã hóa nếu không có trong bảng chữ cái
            encrypted_text.append(output_letter)
        return "".join(encrypted_text)

    def decrypt_text(self, text: str, key: int) -> str:
        text = text.upper()
        decrypted_text = []
        for letter in text:
            if letter in self.alphabet:
                letter_index = self.alphabet.index(letter)
                output_index = (letter_index - key) % len(self.alphabet)
                output_letter = self.alphabet[output_index]
            else:
                output_letter = letter  # Không giải mã nếu không có trong bảng chữ cái
            decrypted_text.append(output_letter)
        return "".join(decrypted_text)
