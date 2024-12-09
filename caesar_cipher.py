import pyperclip

#message = input("What do you want to encrypt/decrypt: ")
file = open('bible.txt', 'r')
content = file.read()
file.close()
message = content

key = input("What do you want to be your key?: ")

mode = input('Do you want to encrypt or decrypt?: ')

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?,".@#$%^&*()_-+={}[]|\:;/~`><'
translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)
            
        if mode == 'encrypt':
            translatedIndex = symbolIndex + int(key)
                
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - int(key)
                
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
                
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)
                
        translated += SYMBOLS[translatedIndex]
    else:
        translated += symbol
        
print(f'This is your {mode}ion: {translated}')
pyperclip.copy(translated)
        