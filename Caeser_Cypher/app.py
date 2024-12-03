import art

print(art.logo)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction=input("Type 'encode' to encode and 'decode' to decode: \n").lower()
text=input("Type your message: \n").lower()
shift=int(input("Enter the shift number: \n"))

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")
#
# def decrypt(cipher_text, shift_amount):
#     original_text=""
#     for letter in cipher_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)
#         original_text += alphabet[shifted_position]
#     print(f"Here is the decoded result: {original_text}")

# if direction=="encode":
#     encrypt(original_text=text, shift_amount=shift)
# elif direction=="decode":
#     decrypt(cipher_text=text, shift_amount=shift)
# else:
#     print("Enter a valid direction")

def caesar(original_text, shift_amount, encode_or_decode):
    cipher_text = ""
    for letter in original_text:

        if encode_or_decode == "decode":
            shift_amount *= -1

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {cipher_text}")

caesar(text, shift, direction)