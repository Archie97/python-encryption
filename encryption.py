alphabet='abcdefghijklmnopqrstuvwxyz'
key=2
newMessage=''
message=input('User, please enter a message: ')

for character in message:
    position=alphabet.find(character)
    newPosition=(position+key)%26
    newCharacter=alphabet[newPosition]
    newMessage += newCharacter


print("the encrypted message is : ",newMessage)
