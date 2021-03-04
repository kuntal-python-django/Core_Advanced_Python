from cryptography.fernet import Fernet

key = Fernet.generate_key()
# Stroing Key
fp = open("key.txt","w+")
fp.write(key.decode("utf-8"))
fp.close()


def Encode():
    f = Fernet(key)
    message = input("Enter Your Message : \n")
    message = message.encode("utf-8")
    token = f.encrypt(message)
    encodeMessage = token.decode("utf-8")
    print("Your Encode Message is : ", encodeMessage)
    fp = open("Message.txt","w+")
    fp.write(token.decode("utf-8"))
    fp.close()


def Decode():
    fp = open("key.txt", "r")
    key = fp.read()
    f = Fernet(key)
    fp = open("Message.txt", "r")
    token = fp.read()
    decodeMessage = f.decrypt(token.encode("utf-8"))
    print("You Decode Message is : ", decodeMessage.decode("utf-8"))


Encode()
Decode()