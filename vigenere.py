import string

alpha = list(string.ascii_lowercase)

#TODO
#make the program not break when it encounters a character not in the alphabet
#do the decrypt program
#comment everything so when I go back through it I know what's going on

    
def encrypt(cipher, message):
    cipher = cipher.lower()
    message = message.lower()
    key_len = len(cipher)
    ciphertext = ''
    int_message = [alpha.index(i) for i in message]
    int_cipher = [alpha.index(i) for i in cipher]
        
    for character in range(len(int_message)):
        print(int_message[character])
        
        val = (int_message[character] + int_cipher[character % key_len]) % 26    
        ciphertext += alpha[val]    
        
    return ciphertext

            
            
def decrypt(cipher, cipherText):
    cipher = cipher.lower()
    message = message.lower()
    key_len = len(cipher)
    message = ''
    int_cipher = [alpha.index(i) for i in cipher]
    int_cipherText = [alpha.index(i) for i in cipherText]
    
    for character in range(len(int_cipherText)):
        val = 
    
    
    
    
#print(encrypt('key', 'hello'))    # Test command for testing the execution of the encrypt and decrypt functions
#print( [string.ascii_lowercase[i:] + string.ascii_lowercase[:i] for i in range(len(string.ascii_lowercase))])    #tableu generation
    
##User input handling portion of the progam
userinput = input("Welcome to the vigenere cipher program. Type 'help' for help using the program, or continue using it if you already know how. To exit, type CTRL + C\n")
while True:
    
    try:    
        if userinput == 'help':
            print("encrypt [ciphertext] - encrypt a block of text, which you enter after inputting the ciphertext\n"
                  "decrypt [ciphertext] - decrypt a block of text, which you enter after inputting the ciphertext\n"
                  "help  - output this menu")
            userinput = input()
            
        elif userinput[:7] == 'encrypt':
            cipherText = userinput[8:]
            if cipherText == '':
                print("you didn't enter a ciphertext")
            else:
                message = input("Please enter your message\n")  #replace this with the encrypt algorithm
                
                print(encrypt(cipherText, message))
            
            userinput = input()
            
        elif userinput == 'decrypt':
            cipherText = userinput[8:]
            if cipherText == '':
                print("you didn't enter a ciphertext")
            else:
                print("Please enter your message")    #replace this with the encrypt algorithm
                
                encrypt(cipherText, userinput)
            userinput = input()            
            
        elif userinput == 'crack':
            userinput = input("haha you think this program actually has this feature\n")
            
        #elif userinput == 'exit':
            #sys.exit()
            
                        
        else:
            userinput = input("You didn't enter a command I recognize. Type help to see what commands are availible\n")
    
    
                
    except:
        print("fuck you")
        userinput = ''