import qrcode

#Taking UPI ID as a Input
upi_id = input("Enter your UPI ID =")

#upi://Pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#Defining the payment and URL based on UPI Id and payment app

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipent%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipent%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipent%20Name&mc=1234'

#create QR codes for each payment app

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make (google_pay_url)

#save the qr code to the image file

phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

#display the QR code(install pil/ pillow library )
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()