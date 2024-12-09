import random, sys, transcription, transcription_decrypter

frequence = int(input('How many times do we need to test?: '))

def main():
    random.seed(42)
    
    for i in range(frequence):
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()' * random.randint(4, 40)
        
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)
        
        print(f'Test {i + 1}: "{message[:50]}"')
        
        for key in range(1, int(len(message) / 2)):
            encrypted = transcription.encryptmessage(key, message)
            decrypted = transcription_decrypter.decryptmessage(key, encrypted)
            
            if message != decrypted:
                print(f'Mismatch with key: {key} and message: {message}.')
                print('Decrypted as: ' + decrypted)
                sys.exit()
                
if __name__ == '__main__':
    main()
