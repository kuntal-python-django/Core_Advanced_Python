from pyzbar.pyzbar import decode
from PIL import Image

image_path = input("Enter Your QrCode Image Path : \n")

data = decode(Image.open(image_path))
decodeData = data[0][0].decode("utf-8")

f= open("Messgae.txt","w+")
f.write(decodeData)
f.close()
