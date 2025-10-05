import qrcode

# 👉 Replace this with your hosted link (GitHub Pages / Netlify / Vercel link)
url = "https://github.com/manassety/love-project.git"

# Generate QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Save image
img = qr.make_image(fill_color="red", back_color="white")
img.save("love_qr.png")

print("✅ QR code generated and saved as love_qr.png")
