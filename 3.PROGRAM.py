def prepare_input(text):
    text = text.replace(" ", "").upper()
    text = text.replace("J", "I")
    return text
def generate_key_matrix(keyword):
    keyword = prepare_input(keyword)
    key_matrix = []
    for char in keyword:
        if char not in key_matrix:
            key_matrix.append(char)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in key_matrix:
            key_matrix.append(char)
    key_matrix = [key_matrix[i:i+5] for i in range(0, 25, 5)]
    return key_matrix
def find_char_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
def playfair_encrypt(plaintext, key_matrix):
    plaintext = prepare_input(plaintext)
    encrypted_text = ""
    for i in range(0, len(plaintext), 2):
        char1 = plaintext[i]
        char2 = plaintext[i+1] if i+1 < len(plaintext) else 'X'
        row1, col1 = find_char_position(key_matrix, char1)
        row2, col2 = find_char_position(key_matrix, char2)
        if row1 == row2:
            encrypted_text += key_matrix[row1][(col1 + 1) % 5] + key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += key_matrix[(row1 + 1) % 5][col1] + key_matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_text += key_matrix[row1][col2] + key_matrix[row2][col1]
    return encrypted_text
keyword = input("Enter the keyword: ")
plaintext = input("Enter the plaintext: ")
key_matrix = generate_key_matrix(keyword)
encrypted_text = playfair_encrypt(plaintext, key_matrix)
print("Encrypted:", encrypted_text)
