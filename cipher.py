def cipher():
    cipher_key = 5
    
    #initialize empty string to return
    encrypted_cipher = ""
    
    #prompt user for input string
    to_cipher = input("Please enter a senctence: ")
    
    #loop over every character in user inputted string
    for letter in to_cipher:
        
        #conditional statement to check if the character is alphabetical
        if letter.isalpha():
            if letter.isupper():
                letter = chr((ord(letter) - ord('A') + cipher_key) % 26 + ord('A'))
                encrypted_cipher += letter
            elif letter.islower():
                letter = chr((ord(letter) - ord('a') + cipher_key) % 26 + ord('a'))
                encrypted_cipher += letter
        
        #doesn't meet initial condition, not an alphabetical character and will be "appended" to string
        else:
            encrypted_cipher += letter
    #final print statement to display encrypted string
    print("The encrypted sentence is: " + encrypted_cipher)

def main():
        cipher()


main()