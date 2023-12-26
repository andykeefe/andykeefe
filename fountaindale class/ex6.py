import time

def encryptMessage(key, message):
    ciphertext = [''] * key
    for column in range(key):
        currentIndex = column
        while currentIndex < len(message):
            ciphertext[column] += message[currentIndex]
            currentIndex += key
            
    return ''.join(ciphertext)
    
    
def main():
    while True:
        print("Input a message: ")
        plaintext = input()
        print("Length of input: " + str(len(plaintext)))
        
        print("Select a key: ")
        myKey = int(input())

        secretCode = encryptMessage(myKey, plaintext)
        print(secretCode)
        print('')
        time.sleep(2)


if __name__ == '__main__':
    main()
  
