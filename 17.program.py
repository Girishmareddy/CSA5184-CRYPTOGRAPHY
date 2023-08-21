def permutation(initial_value, permutation_table):
    return [initial_value[i - 1] for i in permutation_table]

def key_schedule(key):
    return key[::-1]

def shift(key_half, num_shifts):
    return key_half[num_shifts:] + key_half[:num_shifts]

def des_decrypt(ciphertext, keys):
    initial_permutation_table = [2, 6, 3, 1, 4, 8, 5, 7]
    plaintext = permutation(ciphertext, initial_permutation_table)

    for round_key in keys:
        left_half = plaintext[:4]
        right_half = plaintext[4:]
        expanded_right_half = permutation(right_half, [4, 1, 2, 3, 2, 3, 4, 1])
        xored_right_half = [expanded_right_half[i] ^ round_key[i] for i in range(8)]
        plaintext = right_half + left_half
    final_permutation_table = [4, 1, 3, 5, 7, 2, 8, 6]
    decrypted_text = permutation(plaintext, final_permutation_table)
    return decrypted_text

if __name__ == "__main__":
    ciphertext = [0, 1, 1, 0, 1, 0, 0, 1]
    keys = [
        [1, 0, 1, 0, 0, 1, 1, 0],
        [1, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 0, 1]
    ]  
    decrypted_text = des_decrypt(ciphertext, keys)
    print("Decrypted text:", decrypted_text)
