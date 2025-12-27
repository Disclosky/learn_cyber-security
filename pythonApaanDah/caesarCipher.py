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

inputText = input("Enter text to input: ")
caesarCipherResult = caesarCipher_1(inputText)
print(caesarCipherResult)

#that's for today maybe I will make this showing all 25 possibility
#I know there's someone makes it and AI can do it too, but I just wanna try it myself