import qrcode

def generate_qr_code(data, filename="qr_code.png"):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    return filename

telegram_url = "https://t.me/javohirtursunov"

filename = generate_qr_code(telegram_url)
print('qr code created ==>', filename)