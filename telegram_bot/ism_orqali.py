from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

from static import TEKSHIRUV_BUTTONS, ASOSIY_BUTTONS, GET_BUTTONS
ISM_FAMILIYA, KURS_NOMI, DARS_SOATI, SANA, TEKSHIRUV = range(5)

# ---------------- Sertifikat uchun ---------------------
from sertifikat_uchun import img_writer, qr_code_pechat, image_to_pdf
import time
from datetime import date

# -------------- DB --------------
from db import Database
db = Database("../db.sqlite3")

def get_ism_familiya(update, context):
    full_name = update.message.text
    context.user_data["full_name"] = full_name
    print(full_name)

    if full_name == "❌ Bekor qilish":
        update.message.reply_html(
            text="✅ Amaliyot bekor qilindi.",
            reply_markup=ASOSIY_BUTTONS
        )
        return -1
    elif len(full_name.split(" ")) > 1:
        update.message.reply_html(
            text="<b>📄 Kurs nomini kiriting:\n"
                 "👉 Masalan:</b> Zamonaviy axborot kommunikasiya texnologiyalaridan "
                 "foydalanish o'quv kursi(o'rta)",
            reply_markup=GET_BUTTONS
        )

        return KURS_NOMI
    else:
        update.message.reply_html(
            text="<b>😡 Ism familiyani to'g'ri kiriting:\n"
                 "👉 Masalan:</b> Asliddin Abdujabborov",
            reply_markup=GET_BUTTONS
        )

        return ISM_FAMILIYA

def get_kurs_nomi(update, context):
    kurs_nomi = update.message.text
    context.user_data["kurs_nomi"] = kurs_nomi
    print(kurs_nomi)

    if kurs_nomi == "❌ Bekor qilish":
        update.message.reply_html(
            text="✅ Amaliyot bekor qilindi.",
            reply_markup=ASOSIY_BUTTONS
        )
        return -1

    update.message.reply_html(
        text="<b>⏰ Dars soatini kiriting(raqamlarda):\n"
             "👉 Masalan:</b> 48",
        reply_markup=GET_BUTTONS
    )

    return DARS_SOATI

def get_dars_soati(update, context):
    dars_soati = update.message.text
    context.user_data["dars_soati"] = dars_soati
    print(dars_soati)

    if dars_soati == "❌ Bekor qilish":
        update.message.reply_html(
            text="✅ Amaliyot bekor qilindi.",
            reply_markup=ASOSIY_BUTTONS
        )
        return -1


    today = date.today().strftime("%d.%m.%Y")
    if str(dars_soati).isnumeric():
        update.message.reply_html(
            text="<b>📅 Sanani kiriting yoki \"Bugungi sana\" tugmachasini bosing:\n"
                 f"👉 Masalan:</b> {today}",
            reply_markup=ReplyKeyboardMarkup([
                [KeyboardButton(text=f"{today}")]
            ], resize_keyboard=True, one_time_keyboard=True)
        )

        return SANA
    else:
        update.message.reply_html(
            text="<b>😡 Dars soatini raqamda kiriting:\n"
                 "👉 Masalan:</b> 48",
            reply_markup=GET_BUTTONS
        )

        return DARS_SOATI

def get_sana(update, context):
    sana = update.message.text
    context.user_data["sana"] = sana
    print(sana)

    if sana == "❌ Bekor qilish":
        update.message.reply_html(
            text="✅ Amaliyot bekor qilindi.",
            reply_markup=ASOSIY_BUTTONS
        )
        return -1

    if len(str(sana).split(".")) == 3 and len(str(sana)) < 11:
        update.message.reply_html(
            text=f"<b>⚙️ Ma'lumotlar to'g'riligini tekshiring:</b>\n\n"
                 f"👨‍🎓 <b>Ism:</b> {context.user_data['full_name']}\n"
                 f"📄 <b>Kurs nomi:</b> {context.user_data['kurs_nomi']}\n"
                 f"<b>⏰ Dars soati:</b> {context.user_data['dars_soati']}\n"
                 f"📅 <b>Sana:</b> {context.user_data['sana']}\n\n"
                 f"Agar barcha ma'lumotlar to'g'ri bo'lsa <b>\"✅ Yaratish\"</b> aks xolda \n"
                 f"<b>\"❌ Bekor qilish\"</b> tugmasini bosing.",
            reply_markup=TEKSHIRUV_BUTTONS
        )
        return TEKSHIRUV
    else:
        today = date.today().strftime("%d.%m.%Y")
        update.message.reply_html(
            text="<b>😡 Sanani to'g'ri kiriting:\n"
                 f"👉 Masalan:</b> {today}",
            reply_markup=ReplyKeyboardMarkup([
                [KeyboardButton(text=f"{today}")]
            ], resize_keyboard=True, one_time_keyboard=True)
        )

        return SANA

def tekshiruv(update, context):
    xabar = update.message.text
    print("tekshiruv")
    print(xabar)

    if xabar == "✅ Yaratish":
        tayyorlanmoqda = update.message.reply_html(
            text="<b>⚙️ Tayyorlanmoqda...</b>"
        )


        nomerlar = db.get_nomers()
        nomerlar_list = []

        for i in nomerlar:
            nomerlar_list.append(i['nomer'])
        if len(nomerlar_list) == 0:
            hozirgi_nomer = "1122001"
        else:
            hozirgi_nomer = int(max(nomerlar_list)) + 1

        if hozirgi_nomer not in nomerlar_list:
            hozirgi_nomer = str(hozirgi_nomer)

            img_writer(
                name=context.user_data['full_name'],
                kurs_nomi=context.user_data['kurs_nomi'],
                kurs_soati=context.user_data['dars_soati'],
                data=context.user_data['sana'],
                seriya=f"0{hozirgi_nomer}"
            )
            time.sleep(0.1)
            qr_code_pechat(context.user_data['full_name'], f"http://127.0.0.1:8000/success/0{hozirgi_nomer}")
            time.sleep(0.1)
            image_to_pdf(context.user_data['full_name'], f"0{hozirgi_nomer}")
            time.sleep(0.1)

            update.message.reply_document(
                document=open(f"../media/pdf/0{hozirgi_nomer}.pdf", "r+b"),
                caption=f"👨‍🎓 <b>Ism:</b> {context.user_data['full_name']}\n"
                        f"🆔 <b>Seriya nomer:</b> 0{hozirgi_nomer}",
                parse_mode="HTML",
                reply_markup=ASOSIY_BUTTONS
            )
            context.bot.deleteMessage(
                message_id=tayyorlanmoqda.message_id,
                chat_id=update.effective_user.id
            )


            db.create_sertificate(
                nomer=f"0{hozirgi_nomer}",
                url=f"http://127.0.0.1:8000/success/0{hozirgi_nomer}",
                ism_familiya=context.user_data['full_name'],
                kurs_nomi=context.user_data['kurs_nomi'],
                kurs_soati=context.user_data['dars_soati'],
                upload_link=f"http://127.0.0.1:8000/media/pdf/0{hozirgi_nomer}.pdf",
                sana=context.user_data['sana']
            )
        print("Success")
        return -1
    elif xabar == "❌ Bekor qilish":
        update.message.reply_html(
            text="✅ Amaliyot bekor qilindi.",
            reply_markup=ASOSIY_BUTTONS
        )
        return -1