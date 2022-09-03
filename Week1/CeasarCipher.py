#precondition: message must be have only lowercase letters
def encode (message: str, shift: int):
    alphabeth = "abcdefghijklmnopqrstuvwxyz"
    encryptedMessage = ""
    for letter in message:
        #find index
        position = -1
        i = 0;
        while (position == -1):
            if(letter == alphabeth[i]):
                position = i
            i+=1
        #add shifted letter
        encryptedMessage += alphabeth[(position + shift)%26]
    return encryptedMessage;
result = encode("helloworld", 2)
print(result)
encode(result, -2) 