from telegram import ReplyKeyboardMarkup, KeyboardButton

ASOSIY_BUTTONS = ReplyKeyboardMarkup([
    [KeyboardButton("๐ Ism familiya"), KeyboardButton("๐ Excel orqali")],
    [KeyboardButton("๐งน Sertifikatni o'chirish")]
], resize_keyboard=True)

TEKSHIRUV_BUTTONS = ReplyKeyboardMarkup([
    [KeyboardButton("โ Yaratish"), KeyboardButton("โ Bekor qilish")]
], resize_keyboard=True)


GET_BUTTONS = ReplyKeyboardMarkup([
    [KeyboardButton("โ Bekor qilish")]
], resize_keyboard=True)