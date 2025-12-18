import qrcode

qr = qrcode.make("www.youtube.com")
qr.save("test.png")