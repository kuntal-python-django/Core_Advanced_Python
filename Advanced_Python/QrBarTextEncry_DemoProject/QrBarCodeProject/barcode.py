'''
barcode_type='qrcode'
barcode_type='azteccode'
barcode_type='pdf417'
barcode_type='code128' <-- Bar Code
'''
import treepoem

data = input("Enter Your Message : \n")

image = treepoem.generate_barcode(barcode_type='code128', data=data)
image.convert('1').save('barcode.png')
