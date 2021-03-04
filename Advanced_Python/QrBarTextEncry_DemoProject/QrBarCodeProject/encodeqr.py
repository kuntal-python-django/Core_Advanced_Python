'''
ERROR_CORRECT_L = About 7% or less errors can be corrected.
ERROR_CORRECT_M = About 15% or less errors can be corrected.
ERROR_CORRECT_Q = About 25% or less errors can be corrected.
ERROR_CORRECT_H = About 30% or less errors can be corrected.

fill_color and back_color = Can change the background and the painting color of the QR,
                             when using the default image factory.

The version parameter is an integer from 1 to 40 that controls the size of the QR Code 
(the smallest, version 1, is a 21x21 matrix). Set to None and use the fit parameter 
when making the code to determine this automatically.

The box_size parameter controls how many pixels each “box” of the QR code is.

The border parameter controls how many boxes thick the border should be
(the default is 4, which is the minimum according to the specs

'''

import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=5,
)

data = input("Enter Your Message : \n")
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr.png")
img.show()
