from PIL import ImageFont, ImageDraw

import qrcode
from PIL import Image

def img_writer(name, kurs_nomi, kurs_soati, data, seriya):
    width, height = 3431, 2431
    font_size = 90

    img = Image.open("./high_template.jpg")
    draw = ImageDraw.Draw(img)
    font1 = ImageFont.truetype("./fonts/Roboto-MediumItalic.ttf", font_size)
    font2 = ImageFont.truetype("./fonts/Roboto-Medium.ttf", 65)
    font3 = ImageFont.truetype("./fonts/Roboto-Medium.ttf", 70)
    font4 = ImageFont.truetype("./fonts/Roboto-Medium.ttf", 60)

    w1, h1 = draw.textsize(text=name, font=font1)
    w2, h2 = draw.textsize(text=kurs_nomi, font=font2)
    w3, h3 = draw.textsize(text=kurs_soati, font=font3)
    w4, h4 = draw.textsize(text=kurs_soati, font=font3)

    draw.text(((width - w1) / 2, ((height - h1) / 2 - 50)), text=name, fill='#000', font=font1)
    draw.text(((width - w2) / 2, ((height - h2) / 2 + 110)), text=kurs_nomi, fill='#000', font=font2)
    draw.text(((width - w3) / 4 - 90, ((height - h3) / 2 + 285)), text=kurs_soati, fill='#000', font=font3)
    draw.text(((width - w4) / 2 - 200, ((height - h4) / 2 + 960)), text=f"{data} | № {seriya}", fill='#000', font=font4)

    # saved_name_list = []
    # for i in name.split():
    #     if i == "'" or i == " ":
    #         pass
    #     else:
    #         saved_name_list.append()
    # saved_name = "".join(saved_name_list)
    img.save(f'generated-certificates/{name}.jpg')

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

def image_to_pdf(name, seriya_nomer):
    # saved_name_list = []
    # for i in name.split():
    #     if i == "'" or i == " ":
    #         pass
    #     else:
    #         saved_name_list.append()
    # saved_name = "".join(saved_name_list)

    image = Image.open(f"{save_path}/qr_{name}.jpg")
    pdf = image.convert('RGB')
    pdf.save(f'../media/pdf/{seriya_nomer}.pdf')

# img_writer(
#     name="Abdujabborov Asliddin Komil o'g'li",
#     kurs_nomi="Ishlab chiqarish korxonalarini raqamlashtirish, 1S-ERP dasturini o'rganish",
#     kurs_soati="48",
#     data_and_seriya="24.11.2022 | № 01122001"
# )