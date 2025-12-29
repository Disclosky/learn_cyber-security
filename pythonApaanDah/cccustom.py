def caesarCipher_showAll(text):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabetUpper = alphabet.upper()

    attempt = 1

    while attempt <= 25:
        result = ""
        for char in text:
            if char.islower():
                index = alphabet.find(char)
                newIndex = (index - attempt) % 26
                result += alphabet[newIndex]
            elif char.isupper():
                index = alphabetUpper.find(char)
                newIndex = (index - attempt) % 26
                result += alphabetUpper[newIndex]
            else:
                result += char
        print(f'{attempt:2} {result}')
        attempt += 1
    return
#I just realize that this function does not need to shift backward..
#since it print all the result so its doesn't matter

#then I will try to make a customate shift encryption
def caesarCipher_x(text, number):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabetUpper = alphabet.upper()

    result = ""

    for char in text:
        if char.islower():
            index = alphabet.find(char)
            newIndex = (index + number) % 26
            result += alphabet[newIndex]
        elif char.isupper():
            index = alphabetUpper.find(char)
            newIndex = (index + number) % 26
            result += alphabetUpper[newIndex]
        else:
            result += char
	
    print(result)
    
    return
    

#inputText = input("Enter text to input: ")
#shift = int(input("Shift/Key: "))
#caesarCipherResult = caesarCipher_x(inputText, shift)
#print(caesarCipherResult)

def encryptMode():
    return



def decryptMode():
    inputText = str(input("Enter text to decrypt: "))
    caesarCipher_showAll(inputText)
    
    return

while True:
    inputCommand = str(input("What you wanna do?[e/d] "))
    if inputCommand.lower() == "e":
        encryptMode()
        break
    elif inputCommand.lower() == "d":
        decryptMode()
        break
    else:
        continue

