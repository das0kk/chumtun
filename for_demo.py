
alphabet = 'ABCDEFGHIJKLMNOPQRSZTUVWXY'
key = 3
original_message = 'I love programming'
encrypted_message = ''

original_message = original_message.upper()
print(original_message)

for character in original_message:
    new_character = ''
    if character in alphabet:
        original_position = alphabet.find(character)
        new_position = original_position + key
        if new_position > len(alphabet) - 1:
            new_position = original_position + key - len(alphabet)
            new_character = alphabet(new_position)
print(encrypted_message)
