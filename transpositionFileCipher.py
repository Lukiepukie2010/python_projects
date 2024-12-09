import time, os, sys, transcription, transcription_decrypter

def main():
    inputfilename = input('What is the name of the (text) file? FE: xxx.txt ')
    #if not inputfilename.endswith('.txt'):
      #  print('You have to put a text file!!!')
      #  sys.exit()
    mymode = input('Would you like to encrypt or decrypt? ')
    outputname = f'{inputfilename}.{mymode}ed.txt'
    mykey = int(input('What is your key?: '))
    
    if not os.path.exists(inputfilename):
        print(f'The file {inputfilename} does not exist.')
        sys.exit()

    if os.path.exists(outputname):
        print(f'This will overwrite file {outputname}. (C)ontinue or (Q)uit? ')
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()
            
    fileobj = open(inputfilename, 'r')
    content = fileobj.read()
    fileobj.close()
    print(f'{mymode}ing........................................................................................')
    
    startTime = time.time()
    if mymode == 'encrypt':
        translated = transcription.encryptmessage(mykey, content)
    elif mymode == 'decrypt':
        translated = transcription_decrypter.decryptmessage(mykey, content)
    totaltime = round(time.time() - startTime, 2)
    print(f'{mymode}ion time: {totaltime}.')
    
    outputfile = open(outputname, 'w')
    outputfile.write(translated)
    outputfile.close()
    
    print(f'Done {mymode}ing {inputfilename} ({len(content)} characters)')
    print(f'{mymode}ed file: {outputname}')
    
if __name__ == '__main__':
    main()