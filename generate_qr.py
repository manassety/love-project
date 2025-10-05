import qrcode

# 🔗 URL of your hosted HTML webpage
url = "https://manassety.github.io/love-project/"

# Create a new QR code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add your webpage link
qr.add_data(url)
qr.make(fit=True)

# Customize color (optional)
img = qr.make_image(fill_color="red", back_color="white")

# Save the QR image
img.save("love_qr.png")

print("✅ QR connected! Scan love_qr.png to open your live webpage 💖")
