import qrcode
from PIL import Image
path = "generated-certificates"
save_path = "qr_codli"

def qr_code_pechat(name, seriya):
    img_bg = Image.open(f"{path}/{name}.jpg")

    qr = qrcode.QRCode(box_size=12, border=2)
    qr.add_data(seriya)
    qr.make()
    img_qr = qr.make_image()

    width, height = 3431, 2431
    pos = (width-700, height-700)
    img_bg.paste(img_qr, pos)
    img_bg.save(f"{save_path}/qr_{name}.jpg")

def image_to_pdf(name):
    image = Image.open(f"{save_path}/qr_{name}.jpg")
    pdf = image.convert('RGB')
    pdf.save(f'pdf/{name}.pdf')

# qr_code_pechat("Abdujabborov Asliddin Komil o'g'li", "https://asliddinweb.uz/success/01122001")