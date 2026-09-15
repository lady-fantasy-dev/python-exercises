# Write a program to generate a QR code based on user input, such as text or a URL.
# The QR code should be saved as an image file that can be scanned with a smartphone.

import qrcode

data = input("Please enter the data you'd like to have on your QR code: ")
file_name = input("What would you like to name the QR code image? ")

img = qrcode.make(data)
img.save(f"{file_name}.png")
