import qrcode

data = "https://youtu.be/dQw4w9WgXcQ"

img = qrcode.make(data)

img.save("*yourpath*/troll.png")