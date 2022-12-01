from telegram import ReplyKeyboardMarkup, KeyboardButton

ASOSIY_BUTTONS = ReplyKeyboardMarkup([
    [KeyboardButton("📝 Ism familiya"), KeyboardButton("📈 Excel orqali")],
    [KeyboardButton("🧹 Sertifikatni o'chirish")]
], resize_keyboard=True)

TEKSHIRUV_BUTTONS = ReplyKeyboardMarkup([
    [KeyboardButton("✅ Yaratish"), KeyboardButton("❌ Bekor qilish")]
], resize_keyboard=True)


GET_BUTTONS = ReplyKeyboardMarkup([
    [KeyboardButton("❌ Bekor qilish")]
], resize_keyboard=True)