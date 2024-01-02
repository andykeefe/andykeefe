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
        if len(plaintext) > 10:
            while myKey >= len(plaintext) - 3:
                print("Key is insecure. Enter a smaller key: ")
                myKey = int(input())

        secretCode = encryptMessage(myKey, plaintext)
        print(secretCode)
        print('')
        time.sleep(2)


if __name__ == '__main__':
    main()
  
