def cipher(text, shift, decrypt=False):
  result = ""
  if decrypt:
    shift = -shift
  for char in text:
    if char.isalpha():
      shift_base = ord('a') if char.islower() else ord('A')
      result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
    else:
      result += char
  return result


plaintext = input("Enter text to be encrypted: ")
shift = 3
encrypted_text = cipher(plaintext, shift)
print(f"Encrypted: {encrypted_text}")


decrypted_text = cipher(encrypted_text, shift, decrypt=True)
print(f"Decrypted: {decrypted_text}")

