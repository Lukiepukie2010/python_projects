import pyperclip, sys, transpositionFileCipher as trans


def main():
    mymessage = input('What is your message to encrypt? (type "file" to encrypt or decrypt a file) ')
    if mymessage == 'file':
        trans.main()
        sys.exit()
    mykey = int(input('What will be your key? '))

    ciphertext = encryptmessage(mykey, mymessage)
    
    print('Your ciphertext is: ' + ciphertext + '|')
    pyperclip.copy(ciphertext)
    
def encryptmessage(key, message):
    ciphertext = [''] * key
    
    for column in range(key):
        currentIndex = column
        
        while currentIndex < len(message):
            ciphertext[column] += message[currentIndex]
            currentIndex += key
            
    return ''.join(ciphertext)

if __name__ == '__main__':
    main()