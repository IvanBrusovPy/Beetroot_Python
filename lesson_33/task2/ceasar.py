def encrypt(s, text):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if not char.isalnum():
            result += char
        elif char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
    return result
