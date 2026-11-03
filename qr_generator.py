import qrcode

data = input("Enter your mobile number: ")

qr = qrcode.make(data)

qr.save("fake.no.png")

print("QR code successfully created!")