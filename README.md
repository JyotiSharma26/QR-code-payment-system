# QR Code Payment System

## Description
The QR Code Payment System is a Python project that generates QR codes for payment transactions. This project leverages the `qrcode` library to create QR codes and the `Pillow` library to display them. The generated QR codes can be used for seamless and contactless payments.

## Features
- Generate QR codes for payment transactions.
- Save QR codes as image files.
- Display QR codes using the `Pillow` library.

import qrcode
from PIL import Image

Here's a simple example of how to use the application to generate and display a QR code for a payment:

# Payment information
payment_info = 'upi://pay?pa={upi_id}&pn=Recipent%20Name&mc=1234'


# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image file
img.save("payment_qr.png")

# Display the image using Pillow
img.show()
