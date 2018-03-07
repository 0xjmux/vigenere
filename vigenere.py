import string

alpha = list(string.ascii_lowercase)

#TODO
#make the program not break when it encounters a character not in the alphabet
#Crack feature???
    
def encrypt(cipher, message):
    cipher = cipher.lower().replace(' ','')         #converts all letters to lowercase in the cipher, removes all spaces
    message = (message.lower()).replace(' ','')     #converts all letters to lowercase in the message, removes all spaces
    key_len = len(cipher)                           #finds the length of the key
    ciphertext = ''                                    
    int_message = [alpha.index(i) for i in message] #turns the message into a list with each character being a single item
    int_cipher = [alpha.index(i) for i in cipher]   #does pretty much the same thing for the cipher
        
    for character in range(len(int_message)):       #iterates through the message
        val = (int_message[character] + int_cipher[character % key_len]) % 26    #The actual algorithm
        ciphertext += alpha[val]                    #appends each character to the final output
    return ciphertext

                
def decrypt(cipher, cipherText):
    cipher = cipher.lower().replace(' ','')
    cipherText = (cipherText.lower()).replace(' ','')
    key_len = len(cipher)
    message = ''
    int_cipher = [alpha.index(i) for i in cipher]
    int_cipherText = [alpha.index(i) for i in cipherText]
    
    for character in range(len(int_cipherText)):
        val = (int_cipherText[character] - int_cipher[character % key_len]) % 26
        message += alpha[val] 
    return message
    
    
#User input handling portion of the progam
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
                print("you didn't enter a cipher")
            else:
                message = input("Please enter your message\n")  
                
                print(encrypt(cipherText, message))
            
            userinput = input()
            
        elif userinput[:7] == 'decrypt':
            cipher = userinput[8:]
            if cipher == '':
                print("you didn't enter a cipher")
                
            else:
                message = input("Please enter the encrypted ciphertext\n")    
                
                print(decrypt(cipher, message)) 
            userinput = input()
            
        elif userinput == 'crack':
            userinput = input("haha you think this program actually has this feature\n")
            
                        
        else:
            userinput = input("You didn't enter a command I recognize. Type help to see what commands are availible\n")       
    except:         #my brilliant error handling system
        print("fuck you")
        userinput = ''