def decrypt(message):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            shifted_char = chr((ord(char) - 97 - 5) % 26 + 97)
            decrypted_message += shifted_char
        else:
            decrypted_message += char
    return decrypted_message

chat = """xfqfr bfmdz
gjxtp lzj rfz ifkyfw jxi snm
gwt, gjxtp qz rfz rfpfs in bfwlty lfp?
fpz xfdfsl pfrz, rfz lfp ofin ufhfwpz
dfsl pnwnr xynhpjw otrtp pz pnhp ifwn lwzu"""

decrypted_chat = ""
for line in chat.split("\n"):
    decrypted_chat += decrypt(line) + "\n"

print(decrypted_chat)