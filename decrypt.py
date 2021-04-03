
def decrypt_cc(encrypted_message, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSZTUVWXY'
    original_message = ''
    encrypted_message = encrypted_message.upper()

    for encrypted_character in encrypted_message:

        original_character = ''

        if encrypted_character in alphabet:
            encrypted_character_pos = alphabet.find(encrypted_character)
            original_character_pos = encrypted_character_pos - key
            if original_character_pos < 0:
                original_character_pos = original_character_pos + len(alphabet)

            original_character = alphabet[original_character_pos]
        else:
            original_character = encrypted_character

        original_message = original_message + original_character

    return original_message


#############################################################
key = 3
encrypted_message = 'L ORYH STRJTDPPLQJ'
print(decrypt_cc(encrypted_message, key))
