
#Ceaser Cypher
def ceaser_cypher(message, shift, encrypt):
    # message: String
    # shift: int
    # encrypt: bool
    # 
    # ceaser_cypher takes a string and shifts each character by the shift amount either forward
    # or backwards depending on whether encrypt is true or false.
    # 
    # ceaser_cypher() returns the new string and prints it off

    placeholder = 0
    newMessage = ""

    #if we're encrypting
    if(encrypt):
        for element in range(0, len(message)):
            
            placeholder = ord(message[element])

            placeholder += shift

            if placeholder > 126:
                placeholder -= 95

            newMessage += chr(placeholder)

    #If we're decrypting
    else:
        for element in range(0, len(message)):
            
            placeholder = ord(message[element])

            placeholder -= shift

            if placeholder < 32:
                placeholder += 95

            newMessage += chr(placeholder)    
    
    print(newMessage)
    return newMessage


#Vigenere Cypher
def vigenere_cypher(message, keyword, encrypt):
    newMessage = ""

    #If we're encrypting
    if encrypt:
        for element in range(0, len(message)):
            
            placeholder = ord(message[element])

            placeholder += ord(keyword[element%len(keyword)]) - 32

            if placeholder > 126:
                placeholder -= 95

            newMessage += chr(placeholder)    
    #If we're decrypting
    else:
        for element in range(0, len(message)):
            
            placeholder = ord(message[element])

            placeholder -= ord(keyword[element%len(keyword)]) - 32

            if placeholder < 32:
                placeholder += 95

            newMessage += chr(placeholder)  


    print(newMessage)
    return newMessage

#~~~~~~~~~~~~~~Testing~~~~~~~~~~~~~~~~~

#My vigenere cypher does not use the function for ceaser cypher directly, but uses the same process
vigenere_cypher("attackatdawn", "lemon", True) 
vigenere_cypher("NZbQRXGbTPdT", "lemon", False)

ceaser_cypher("attackatdawn", 5, True)
ceaser_cypher("fyyfhpfyif|s", 5, False)

