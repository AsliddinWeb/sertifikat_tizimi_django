import time

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from telegram import ReplyKeyboardRemove


from static import ASOSIY_BUTTONS
from config import TOKEN, ADMIN_LIST
from ism_orqali import get_ism_familiya, get_kurs_nomi, get_dars_soati, get_sana, tekshiruv

ISM_FAMILIYA, KURS_NOMI, DARS_SOATI, SANA, TEKSHIRUV = range(5)

def start_handler(update, context):
    print("/start")
    user = update.effective_user

    if user.id in ADMIN_LIST:
        update.message.reply_html(
            text="📨 <b>Assalom aleykum, admin!\n"
                "Hush kelibsiz!</b>",
            reply_markup=ASOSIY_BUTTONS
        )

        # update.message.reply_document(
        #     document=open(f"pdf/Asliddin Abdujabborov.pdf", "r+b"),
        #     caption="Asliddin Abdujabborov"
        # )

def ism_handler(update, context):
    update.message.reply_html(
        text="<b>🧧 Sertifikat oluvchining ism familiyasini kiriting:\n"
             "👉 Masalan:</b> Asliddin Abdujabborov",
        reply_markup=ReplyKeyboardRemove()
    )

    return ISM_FAMILIYA
    # tayyorlanmoqda = update.message.reply_html(
    #     text="Tayyorlanmoqda..."
    # )
    #
    # run(name)
    # time.sleep(0.1)
    # qr_code_pechat(name, "https://asliddinweb.uz")
    # time.sleep(0.1)
    # image_to_pdf(name)
    # time.sleep(1)
    #
    #
    # update.message.reply_document(
    #     document=open(f"pdf/{name}.pdf", "rb"),
    #     caption=name
    # )
    # context.bot.deleteMessage(
    #     message_id=tayyorlanmoqda.message_id,
    #     chat_id=update.effective_user.id
    # )
    # print("Success")

def cansel_handler(update, context):
    return -1

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_handler))
    # dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

    dispatcher.add_handler(ConversationHandler(
        entry_points=[MessageHandler(Filters.text("📝 Ism familiya"), ism_handler)],
        states={
            ISM_FAMILIYA: [MessageHandler(Filters.text, get_ism_familiya)],
            KURS_NOMI: [MessageHandler(Filters.text, get_kurs_nomi)],
            DARS_SOATI: [MessageHandler(Filters.text, get_dars_soati)],
            SANA: [MessageHandler(Filters.text, get_sana)],
            TEKSHIRUV: [MessageHandler(Filters.text, tekshiruv)],
        },
        fallbacks=[CommandHandler('cansel', cansel_handler)]
    ))

    

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()