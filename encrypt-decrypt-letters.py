alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()


def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")

def decrypt(plain_text, shift_amount):
  decoded_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    decrypted_position = position - shift_amount
    old_letter = alphabet[decrypted_position]
    decoded_text += old_letter
  print(f"The decoded text is {decoded_text}")
    
if direction == "encode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(plain_text=text, shift_amount=shift)
  
if direction == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    decrypt(plain_text=text, shift_amount=shift)