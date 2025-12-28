def caesarCipher_1(text):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabetUpper = alphabet.upper()

    result = ""

    for char in text:
        if char.islower():
            index = alphabet.find(char)
            newIndex = (index + 1) % 26
            result += alphabet[newIndex]
        elif char.isupper():
            index = alphabetUpper.find(char)
            newIndex = (index + 1) % 26
            result += alphabetUpper[newIndex]
        else:
            result += char
    return result
#it's just for testing...

#that's for today maybe I will make this showing all 25 possibility
#I know there's someone makes it and AI can do it too, but I just wanna try it myself

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

inputText = input("Enter text to input: ")
caesarCipherResult = caesarCipher_showAll(inputText)

#I just realize that this function does not need to shift backward.. 
#since it print all the result so its doesn't matter

#then I will try to make a customate shift encryption