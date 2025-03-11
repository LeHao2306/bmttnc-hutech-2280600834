class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        if num_rails <= 1:
            return plain_text

        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # 1: xuống, -1: lên

        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        if num_rails <= 1:
            return cipher_text

        # Bước 1: Xác định độ dài từng hàng
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # Bước 2: Điền dữ liệu vào `rails`
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(cipher_text[start:start + length]))  # Chuyển thành list thay vì string
            start += length

        # Bước 3: Đọc dữ liệu theo pattern để giải mã
        plain_text = []
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            if rails[rail_index]:  # Kiểm tra nếu còn phần tử
                plain_text.append(rails[rail_index].pop(0))

            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        return ''.join(plain_text)
