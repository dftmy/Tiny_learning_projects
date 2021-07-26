import qrcode
link = "https://github.com/dftmy/Tiny_learning_projects"
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(link)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode001.png')