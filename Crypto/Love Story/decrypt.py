def to_my_honey(owo):
    return ord(owo) - 0x41

def from_your_lover(uwu):
    return chr(uwu % 26 + 0x41)

def decrypt(encrypted_message):
    original_message = ''
    for heart in range(len(encrypted_message)):
        letters = encrypted_message[heart]
        if not letters.isalpha():
            owo = letters
        else:
            uwu = to_my_honey(letters)
            owo = from_your_lover(uwu - heart)
        original_message += owo
    return original_message

# Given encrypted message
c = "KJOL_T_ZCTS_ZV_CQKLX_NDFKZTUC."

m = decrypt(c)
print(m)

#Output: KIMI_O_SUKI_NI_NATTE_SHIMATTA.
