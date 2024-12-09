import math, pyperclip

def main():
    mymessage = input('What message do you want to decrypt?: ')
    mykey = int(input('What will be your key?: '))
    
    plaintext = decryptmessage(mykey, mymessage)
    
    print('This is your decryptes message: ' + plaintext + '|')
    
    pyperclip.copy(plaintext)
    
def decryptmessage(key, message):
    numofcolumns = int(math.ceil(len(message) / key))
    numofrows = key
    numofshadedboxes = (numofcolumns * numofrows) - len(message)
    
    plaintext = [''] * numofcolumns
    
    column = 0
    row = 0
    
    for symbol in message:
        plaintext[column] += symbol
        column += 1
        
        if (column == numofcolumns) or (column == numofcolumns - 1 and
                                        row >= numofrows - numofshadedboxes):
            column = 0
            row += 1
            
    return ''.join(plaintext)

if __name__ == '__main__':
    main()
                       