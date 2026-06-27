def askInput(prompt, inputType='text', defaultShift=None):
    while True:
        userInput = input(prompt).strip()

        if inputType == 'text':           
            if not userInput:
                print("pls input something!")
                continue
            
            if not any(char.isalpha() for char in userInput):
                print("whaat??")
                continue
            return userInput

        elif inputType == 'number':   
            if not userInput:
                return defaultShift
        
            try:
                number = int(userInput)
                if number == 0 or number == 26 :
                    print("are u kidding me?")
                    continue
                return number
            except:
                print("pls enter a valid number")
                continue


alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetUpper = alphabet.upper()

def caesarCipher_showAll(text):

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

def caesarCipher_x(text, number):

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

while True:
    greetings = askInput("May I help you?[e/d] : ", inputType="text")
    if greetings.lower() == 'e':
        textToEncrypt = askInput("Enter text to encrypt: ", inputType="text")
        shiftTo = askInput("Shift/Key [default=3] : ", inputType="number", defaultShift=3)
        caesarCipher_x(textToEncrypt, shiftTo)
        break
    elif greetings.lower() == 'd':
        textToDecrypt = askInput("Enter text to decrypt: ", inputType="text")
        caesarCipher_showAll(textToDecrypt)
        break
    else:
        continue


#honestly I need to make this to have a maximum input length
#but maybe it's done..
#and I need your feedback!
#or.. maybe not cuz this repo will be private. Thanks! :)