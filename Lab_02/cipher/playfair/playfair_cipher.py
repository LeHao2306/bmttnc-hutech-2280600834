class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        """ Tạo ma trận Playfair 5x5 từ khóa đầu vào """
        key = key.replace("J", "I").upper()  # Chuyển "J" thành "I" và viết hoa
        key_set = set()
        matrix = []

        # Thêm ký tự trong key vào ma trận nếu chưa tồn tại
        for char in key:
            if char not in key_set and char.isalpha():
                key_set.add(char)
                matrix.append(char)

        # Thêm các ký tự còn lại của bảng chữ cái
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for char in alphabet:
            if char not in key_set:
                matrix.append(char)

        # Chia thành ma trận 5x5
        playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        """ Tìm tọa độ của chữ cái trong ma trận Playfair """
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        return None  # Tránh lỗi nếu ký tự không tồn tại

    def preprocess_text(self, text):
        """ Xử lý văn bản: thay J thành I và viết hoa """
        return text.replace("J", "I").upper()

    def playfair_encrypt(self, plain_text, matrix):
        """ Mã hóa văn bản bằng Playfair Cipher """
        plain_text = self.preprocess_text(plain_text)
        encrypted_text = ""

        # Chia thành các cặp ký tự, xử lý ký tự lẻ
        pairs = []
        i = 0
        while i < len(plain_text):
            char1 = plain_text[i]
            char2 = plain_text[i + 1] if i + 1 < len(plain_text) else "X"

            if char1 == char2:
                pairs.append((char1, "X"))
                i += 1
            else:
                pairs.append((char1, char2))
                i += 2

        # Mã hóa từng cặp
        for char1, char2 in pairs:
            row1, col1 = self.find_letter_coords(matrix, char1)
            row2, col2 = self.find_letter_coords(matrix, char2)

            if row1 == row2:  # Cùng hàng
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:  # Cùng cột
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:  # Hình chữ nhật
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        """ Giải mã văn bản bằng Playfair Cipher """
        cipher_text = self.preprocess_text(cipher_text)
        decrypted_text = ""

        # Chia thành các cặp ký tự
        pairs = [(cipher_text[i], cipher_text[i + 1]) for i in range(0, len(cipher_text), 2)]

        # Giải mã từng cặp
        for char1, char2 in pairs:
            row1, col1 = self.find_letter_coords(matrix, char1)
            row2, col2 = self.find_letter_coords(matrix, char2)

            if row1 == row2:  # Cùng hàng
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:  # Cùng cột
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:  # Hình chữ nhật
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]

        # Loại bỏ ký tự 'X' nếu là ký tự đệm
        banro = ""
        for i in range(len(decrypted_text) - 1):
            if decrypted_text[i] == "X" and (i == len(decrypted_text) - 1 or decrypted_text[i - 1] == decrypted_text[i + 1]):
                continue
            banro += decrypted_text[i]

        banro += decrypted_text[-1] if decrypted_text[-1] != "X" else ""

        return banro
