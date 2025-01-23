alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def encode(message, shift_number):
    encoded_message = ""
    for l in message:
        if l in alphabet:
            encoded_message += alphabet[(alphabet.index(l) + shift_number) % len(alphabet)]
        else:
            encoded_message += l
    print(f"Here's the encoded result: {encoded_message}")

def decode(encoded_message, shift_number):
    decoded_message = ""
    for l in encoded_message:
        if l in alphabet:
            decoded_message += alphabet[(alphabet.index(l) - shift_number) % len(alphabet)]
        else:
            decoded_message += l
    print(f"The decoded message is: {decoded_message}")


while True:
    enc_or_dec = input("Type 'encode' to encrypt or 'decode' to decrypt: ").lower()
    
    if enc_or_dec == "encode":
        message = input("Type your message: ").lower()
        shift_number = int(input("Enter the shift number: "))
        encode(message, shift_number)
    elif enc_or_dec == "decode":
        message = input("Type your message: ").lower()
        shift_number = int(input("Enter the shift number: "))
        decode(message, shift_number)
    else:
        print("invalid choice")
    
    
    run_it_back = input("Type 'yes' if you want to go again; otherwise type 'no': ").lower()
    if run_it_back == 'no':
        print("Goodbye")
        break