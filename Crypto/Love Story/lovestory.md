## Challenge Description
Otto and his brothers discover that his friend Siegfried has written a love letter to the girl of his dreams. When he opened it, it was a very cheesy letter, but part of it was encrypted and couldn't be read. And then hearing about the experts at the OSCTF tournament who could decode all codes, he immediately brought the letter to ask you to see it. Don't put the plaintext in flag format.

Ex: the output is HELLO_WORLD, then the flag is OSCTF{HELLO_WORLD}

[Challenge File](https://github.com/user-attachments/files/16215687/letter.1.txt)

## Solution

The hint given was the source code used was
```py
def to_my_honey(owo):
    return ord(owo) - 0x41

def from_your_lover(uwu):
    return chr(uwu % 26 + 0x41)

def encrypt(billet_doux):
    letter = ''
    for heart in range(len(billet_doux)):
        letters = billet_doux[heart]
        if not letters.isalpha():
            owo = letters
        else:
            uwu = to_my_honey(letters)
            owo = from_your_lover(uwu + heart)
        letter += owo
    return letter

m = "REDACTED"

c = encrypt(m)
print(c)
```

Thus by reversing this, we can get our solve script

```py
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
```

This gives us the output KIMI_O_SUKI_NI_NATTE_SHIMATTA. This translates to 
![image](https://github.com/user-attachments/assets/052ef6f1-edca-4401-9e06-7ca4f44d9772)

Our flag is OSCTF{KIMI_O_SUKI_NI_NATTE_SHIMATTA.}
