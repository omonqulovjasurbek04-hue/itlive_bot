import asyncio
import logging, sys, os
from aiogram import Dispatcher, Bot, F
from aiogram.filters import Command
from aiogram.types import (
    Message, ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
)
from dotenv import load_dotenv

load_dotenv()
API = os.getenv("API")
dp = Dispatcher()

# ───────────────────────────────────────────────
# MENU
# ───────────────────────────────────────────────
menu = [
    'IT Live haqida🏫',
    'Kurslar📚',
    'Mentorlar🧑‍🏫',
    "Biz bilan bog`lanish📞",
    "Lokatsiya🚩"
]

Menu = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=item)] for item in menu],
    resize_keyboard=True
)

# ───────────────────────────────────────────────
# KURSLAR
# ───────────────────────────────────────────────
kurslar = [
    "Mobil dasturlash",       # 0
    "Foundation Dasturlash",  # 1
    "Frontend Dasturlash",    # 2
    "Backend Dasturlash",     # 3
    "Full Stack Dasturlash",  # 4
    "Sun'iy intellekt",       # 5
    "Kiber xavfsizlik",       # 6
    "Robototexnika",          # 7
    "Buxgalteriya",           # 8
    "SMM",                    # 9
    "DevOps",                 # 10
    "Arduino",                # 11
    "⬅️ Orqaga"               # 12
]

Kurslar = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=item)] for item in kurslar],
    resize_keyboard=True
)

kurs_malumot = {
    kurslar[0]: {
        "nomi": "📱 Mobil Dasturlash",
        "tavsif": (
            "Flutter yoki React Native yordamida iOS va Android uchun ilovalar yaratishni o'rganasiz.\n\n"
            "✅ Davomiyligi: 6 oy\n"
            "✅ Daraja: Boshlang'ich → O'rta\n"
            "✅ Narxi: 500 000 so'm/oy\n\n"
            "📌 Nimalar o'rganiladi:\n"
            "  • Dart/Flutter asoslari\n"
            "  • UI/UX dizayn tamoyillari\n"
            "  • API integratsiya\n"
            "  • Play Market / App Store'ga chiqarish"
        )
    },
    kurslar[1]: {
        "nomi": "💻 Foundation Dasturlash",
        "tavsif": (
            "Dasturlashga yangi boshlovchilar uchun. Kompyuter va mantiqiy fikrlash asoslarini o'rganasiz.\n\n"
            "✅ Davomiyligi: 3 oy\n"
            "✅ Daraja: Boshlang'ich\n"
            "✅ Narxi: 300 000 so'm/oy\n\n"
            "📌 Nimalar o'rganiladi:\n"
            "  • Algoritmlar va ma'lumotlar tuzilmasi\n"
            "  • Python asoslari\n"
            "  • Git va GitHub\n"
            "  • Muammolarni hal qilish ko'nikmalari"
        )
    },
    kurslar[2]: {
        "nomi": "🌐 Frontend Dasturlash",
        "tavsif": (
            "Zamonaviy web saytlar va veb-ilovalar interfeysini yaratishni o'rganasiz.\n\n"
            "✅ Davomiyligi: 5 oy\n"
            "✅ Daraja: Boshlang'ich → O'rta\n"
            "✅ Narxi: 450 000 so'm/oy\n\n"
            "📌 Nimalar o'rganiladi:\n"
            "  • HTML5 va CSS3\n"
            "  • JavaScript (ES6+)\n"
            "  • React.js framework\n"
            "  • Responsive dizayn\n"
            "  • Figma bilan ishlash"
        )
    },
    kurslar[3]: {
        "nomi": "🖥️ Backend Dasturlash",
        "tavsif": (
            "Server tomoni dasturlash, ma'lumotlar bazasi va API yaratishni o'rganasiz.\n\n"
            "✅ Davomiyligi: 6 oy\n"
            "✅ Daraja: O'rta\n"
            "✅ Narxi: 500 000 so'm/oy\n\n"
            "📌 Nimalar o'rganiladi:\n"
            "  • Python / Node.js\n"
            "  • Django / Express.js\n"
            "  • PostgreSQL / MongoDB\n"
            "  • REST API va JWT\n"
            "  • Docker asoslari"
        )
    },
    kurslar[4]: {
        "nomi": "🚀 Full Stack Dasturlash",
        "tavsif": (
            "Frontend va Backend'ni birgalikda o'rganib, to'liq loyiha yaratasiz.\n\n"
            "✅ Davomiyligi: 10 oy\n"
            "✅ Daraja: O'rta → Yuqori\n"
            "✅ Narxi: 600 000 so'm/oy\n\n"
            "📌 Nimalar o'rganiladi:\n"
            "  • React.js + Node.js\n"
            "  • Ma'lumotlar bazasi (SQL & NoSQL)\n"
            "  • Bulut xizmatlari (AWS/Vercel)\n"
            "  • CI/CD va deployment\n"
            "  • Real loyiha yaratish"
        )
    },
    kurslar[5]: {
        "nomi": "🤖 Sun'iy Intellekt (AI)",
        "tavsif": (
            "Machine Learning va Deep Learning asoslarini o'rganib, AI modellar yaratasiz.\n\n"
            "✅ Davomiyligi: 8 oy\n"
            "✅ Daraja: O'rta → Yuqori\n"
            "✅ Narxi: 700 000 so'm/oy\n\n"
            "📌 Nimalar o'rganiladi:\n"
            "  • Python va matematik asoslar\n"
            "  • Machine Learning (Scikit-learn)\n"
            "  • Deep Learning (TensorFlow/PyTorch)\n"
            "  • NLP va Computer Vision\n"
            "  • ChatGPT API integratsiyasi"
        )
    },
    kurslar[6]: {
        "nomi": "🔐 Kiber Xavfsizlik",
        "tavsif": (
            "Tizimlar va tarmoqlarni himoya qilish, xakerlik hujumlarini aniqlashni o'rganasiz.\n\n"
            "✅ Davomiyligi: 6 oy\n"
            "✅ Daraja: O'rta\n"
            "✅ Narxi: 550 000 so'm/oy\n\n"
            "📌 Nimalar o'rganiladi:\n"
            "  • Tarmoq xavfsizligi asoslari\n"
            "  • Ethical hacking\n"
            "  • Penetration testing\n"
            "  • Kriptografiya\n"
            "  • CTF musobaqalari"
        )
    },
    kurslar[7]: {
        "nomi": "🤖 Robototexnika",
        "tavsif": (
            "Robotlar va avtomatlashtirilgan tizimlarni loyihalash va dasturlashni o'rganasiz.\n\n"
            "✅ Davomiyligi: 6 oy\n"
            "✅ Daraja: Boshlang'ich → O'rta\n"
            "✅ Narxi: 600 000 so'm/oy\n\n"
            "📌 Nimalar o'rganiladi:\n"
            "  • Arduino va Raspberry Pi\n"
            "  • Sensorlar va aktuatorlar\n"
            "  • Robot mexanikasi\n"
            "  • C++ dasturlash\n"
            "  • Real robot loyihalari"
        )
    },
    kurslar[8]: {
        "nomi": "📊 Buxgalteriya",
        "tavsif": (
            "Zamonaviy kompyuter dasturlari yordamida moliyaviy hisobot va buxgalteriya yuritishni o'rganasiz.\n\n"
            "✅ Davomiyligi: 4 oy\n"
            "✅ Daraja: Boshlang'ich\n"
            "✅ Narxi: 350 000 so'm/oy\n\n"
            "📌 Nimalar o'rganiladi:\n"
            "  • 1C Buxgalteriya\n"
            "  • Microsoft Excel (Moliyaviy)\n"
            "  • Soliq hisoboti\n"
            "  • Balans va moliyaviy tahlil\n"
            "  • Onlayn hisob-kitob tizimlari"
        )
    },
    kurslar[9]: {
        "nomi": "📱 SMM (Ijtimoiy Tarmoqlar Menejmenti)",
        "tavsif": (
            "Instagram, Telegram, YouTube va boshqa platformalarda biznesni rivojlantirishni o'rganasiz.\n\n"
            "✅ Davomiyligi: 3 oy\n"
            "✅ Daraja: Boshlang'ich\n"
            "✅ Narxi: 300 000 so'm/oy\n\n"
            "📌 Nimalar o'rganiladi:\n"
            "  • Kontent yaratish strategiyasi\n"
            "  • Targeting va reklama\n"
            "  • Grafik dizayn (Canva)\n"
            "  • Analitika va statistika\n"
            "  • Brend qurish"
        )
    },
    kurslar[10]: {
        "nomi": "⚙️ DevOps",
        "tavsif": (
            "Dasturiy ta'minotni avtomatlashtirilgan holda yetkazib berish va infratuzilma boshqaruvini o'rganasiz.\n\n"
            "✅ Davomiyligi: 7 oy\n"
            "✅ Daraja: O'rta → Yuqori\n"
            "✅ Narxi: 650 000 so'm/oy\n\n"
            "📌 Nimalar o'rganiladi:\n"
            "  • Linux server boshqaruvi\n"
            "  • Docker va Kubernetes\n"
            "  • CI/CD pipeline (Jenkins/GitHub Actions)\n"
            "  • AWS / Google Cloud\n"
            "  • Monitoring (Grafana, Prometheus)"
        )
    },
    kurslar[11]: {
        "nomi": "🔧 Arduino",
        "tavsif": (
            "Arduino platasi yordamida elektron qurilmalar va mini loyihalar yaratishni o'rganasiz.\n\n"
            "✅ Davomiyligi: 3 oy\n"
            "✅ Daraja: Boshlang'ich\n"
            "✅ Narxi: 280 000 so'm/oy\n\n"
            "📌 Nimalar o'rganiladi:\n"
            "  • Elektronika asoslari\n"
            "  • Arduino IDE va C++ asoslari\n"
            "  • Sensorlar (harorat, yorug'lik, harakat)\n"
            "  • LCD va LED boshqaruvi\n"
            "  • Mini amaliy loyihalar"
        )
    },
}

# ───────────────────────────────────────────────
# MENTORLAR
# ───────────────────────────────────────────────
mentorlar_list = [
    "👨‍💻 Asadbek Yusupov",   # 0  – Full Stack
    "👩‍💻 Nilufar Karimova",   # 1  – Frontend
    "👨‍💻 Jasur Toshmatov",    # 2  – Backend
    "👩‍💻 Shahlo Mirzayeva",   # 3  – Mobil
    "👨‍💻 Bobur Xasanov",      # 4  – AI/ML
    "👩‍💻 Malika Ergasheva",   # 5  – SMM
    "👨‍💻 Sarvar Normatov",    # 6  – DevOps
    "👨‍💻 Ulug'bek Qodirov",   # 7  – Kiber Xavfsizlik
    "⬅️ Orqaga"               # 8
]

Mentorlar = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=item)] for item in mentorlar_list],
    resize_keyboard=True
)

mentor_malumot = {
    mentorlar_list[0]: (
        "👨‍💻 Asadbek Yusupov\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎓 Yo'nalish: Full Stack Dasturlash\n"
        "💼 Tajriba: 5 yil\n"
        "🏢 Kompaniya: IT Live O'quv Markazi\n\n"
        "📌 Texnologiyalar:\n"
        "  • React.js, Node.js, PostgreSQL\n"
        "  • Docker, AWS, REST API\n\n"
        "🏆 Yutuqlar:\n"
        "  • 200+ talaba tayyorlagan\n"
        "  • 3 ta yirik korporativ loyiha muallifi\n\n"
        "📬 Telegram: @asadbek_dev"
    ),
    mentorlar_list[1]: (
        "👩‍💻 Nilufar Karimova\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎓 Yo'nalish: Frontend Dasturlash\n"
        "💼 Tajriba: 4 yil\n"
        "🏢 Kompaniya: IT Live O'quv Markazi\n\n"
        "📌 Texnologiyalar:\n"
        "  • HTML5, CSS3, JavaScript\n"
        "  • React.js, Tailwind CSS, Figma\n\n"
        "🏆 Yutuqlar:\n"
        "  • 150+ talaba tayyorlagan\n"
        "  • UX/UI bo'yicha sertifikat (Google)\n\n"
        "📬 Telegram: @nilufar_frontend"
    ),
    mentorlar_list[2]: (
        "👨‍💻 Jasur Toshmatov\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎓 Yo'nalish: Backend Dasturlash\n"
        "💼 Tajriba: 6 yil\n"
        "🏢 Kompaniya: IT Live O'quv Markazi\n\n"
        "📌 Texnologiyalar:\n"
        "  • Python, Django, FastAPI\n"
        "  • PostgreSQL, Redis, Celery\n\n"
        "🏆 Yutuqlar:\n"
        "  • 180+ talaba tayyorlagan\n"
        "  • Xalqaro hackathon g'olibi (2022)\n\n"
        "📬 Telegram: @jasur_backend"
    ),
    mentorlar_list[3]: (
        "👩‍💻 Shahlo Mirzayeva\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎓 Yo'nalish: Mobil Dasturlash\n"
        "💼 Tajriba: 4 yil\n"
        "🏢 Kompaniya: IT Live O'quv Markazi\n\n"
        "📌 Texnologiyalar:\n"
        "  • Flutter, Dart\n"
        "  • Firebase, REST API\n"
        "  • iOS & Android deployment\n\n"
        "🏆 Yutuqlar:\n"
        "  • Play Market'da 5 ta nashr etilgan ilova\n"
        "  • 120+ talaba tayyorlagan\n\n"
        "📬 Telegram: @shahlo_mobile"
    ),
    mentorlar_list[4]: (
        "👨‍💻 Bobur Xasanov\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎓 Yo'nalish: Sun'iy Intellekt / ML\n"
        "💼 Tajriba: 5 yil\n"
        "🏢 Kompaniya: IT Live O'quv Markazi\n\n"
        "📌 Texnologiyalar:\n"
        "  • Python, TensorFlow, PyTorch\n"
        "  • Scikit-learn, OpenCV, NLP\n\n"
        "🏆 Yutuqlar:\n"
        "  • Kaggle Master darajasi\n"
        "  • 2 ta ilmiy maqola muallifi\n\n"
        "📬 Telegram: @bobur_ai"
    ),
    mentorlar_list[5]: (
        "👩‍💻 Malika Ergasheva\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎓 Yo'nalish: SMM & Digital Marketing\n"
        "💼 Tajriba: 5 yil\n"
        "🏢 Kompaniya: IT Live O'quv Markazi\n\n"
        "📌 Ixtisoslik:\n"
        "  • Instagram, Telegram, YouTube\n"
        "  • Kontent strategiya, Targeting\n"
        "  • Canva, CapCut, Figma\n\n"
        "🏆 Yutuqlar:\n"
        "  • 10+ brendga 100K+ auditoriya qo'shgan\n"
        "  • 200+ talaba tayyorlagan\n\n"
        "📬 Telegram: @malika_smm"
    ),
    mentorlar_list[6]: (
        "👨‍💻 Sarvar Normatov\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎓 Yo'nalish: DevOps Engineering\n"
        "💼 Tajriba: 6 yil\n"
        "🏢 Kompaniya: IT Live O'quv Markazi\n\n"
        "📌 Texnologiyalar:\n"
        "  • Linux, Docker, Kubernetes\n"
        "  • AWS, CI/CD, Terraform\n"
        "  • Grafana, Prometheus\n\n"
        "🏆 Yutuqlar:\n"
        "  • AWS Certified Solutions Architect\n"
        "  • 100+ talaba tayyorlagan\n\n"
        "📬 Telegram: @sarvar_devops"
    ),
    mentorlar_list[7]: (
        "👨‍💻 Ulug'bek Qodirov\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎓 Yo'nalish: Kiber Xavfsizlik\n"
        "💼 Tajriba: 7 yil\n"
        "🏢 Kompaniya: IT Live O'quv Markazi\n\n"
        "📌 Ixtisoslik:\n"
        "  • Ethical Hacking, Penetration Testing\n"
        "  • Network Security, Kriptografiya\n"
        "  • CTF musobaqalari\n\n"
        "🏆 Yutuqlar:\n"
        "  • CEH (Certified Ethical Hacker) sertifikati\n"
        "  • Davlat muassasalari uchun audit o'tkazgan\n\n"
        "📬 Telegram: @ulugbek_cyber"
    ),
}


# ───────────────────────────────────────────────
# HANDLERS
# ───────────────────────────────────────────────
@dp.message(Command('start'))
async def start_handler(msg: Message):
    await msg.answer(
        "👋 Salom! IT Live botiga xush kelibsiz!\n"
        "Quyidagi bo'limlardan birini tanlang 👇",
        reply_markup=Menu
    )


@dp.message(F.text.in_(menu))
async def menu_handler(msg: Message):
    T = msg.text

    if T == menu[0]:  # IT Live haqida
        await msg.answer(
            "🏫 IT Live haqida ma'lumot\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "IT Live — axborot texnologiyalari sohasida "
            "jonli va amaliy darslar o'tkaziladigan zamonaviy o'quv markazidir.\n\n"
            "📚 Mavzular:\n"
            "  • Dasturlash (Python, JS, Flutter va boshqalar)\n"
            "  • Web va mobil dasturlash\n"
            "  • Sun'iy intellekt va yangi texnologiyalar\n"
            "  • Grafik dizayn va SMM\n"
            "  • Kiber xavfsizlik va DevOps\n\n"
            "✅ Afzalliklar:\n"
            "  • O'qituvchi bilan jonli muloqot\n"
            "  • Savolga darhol javob\n"
            "  • Ko'plab amaliy mashg'ulotlar\n"
            "  • Sertifikat beriladi\n"
            "  • Ish joyi topishga ko'maklashiladi"
        )

    elif T == menu[1]:  # Kurslar
        await msg.answer("📚 Kurs tanlang 👇", reply_markup=Kurslar)

    elif T == menu[2]:  # Mentorlar
        await msg.answer("🧑‍🏫 Mentor tanlang 👇", reply_markup=Mentorlar)

    elif T == menu[3]:  # Biz bilan bog'lanish
        button = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text='📱 Telegramda yozing', url='https://t.me/+998915093298')]
            ]
        )
        await msg.answer(
            "📞 Biz bilan bog'lanish\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "Kurslar haqida ma'lumot olish yoki ro'yxatdan o'tish uchun:\n\n"
            "📞 Telefon: +998 99 721 20 17\n"
            "📱 Telegram: @itlive\n"
            "📧 Email: info@itlive.uz\n\n"
            "🕐 Ish vaqti: Du–Shan, 09:00 – 18:00",
            reply_markup=button
        )

    elif T == menu[4]:  # Lokatsiya
        photo = FSInputFile('./img/itlve_photo.png')
        await msg.answer_photo(
            photo=photo,
            caption="""
🚩 Bizning Manzilimiz\n
━━━━━━━━━━━━━━━━━━━\n\n
📍 Manzil: Sirdaryo viloyati, Guliston shahri\n
🏢 Bino: IT Live O'quv Markazi, 2-qavat\n
🚆 Mo'ljal: Markaziy bozor yonida\n\n
📍 Xaritada ko'rish uchun quyidagi lokatsiyaga qarang 👇""")
        await msg.answer_location(latitude=40.502711, longitude=68.764823)


@dp.message(F.text.in_(kurslar))
async def kurs_handler(msg: Message):
    T = msg.text

    if T == kurslar[12]:  # Orqaga
        await msg.answer("🏠 Bosh menyu", reply_markup=Menu)
        return

    if T in kurs_malumot:
        info = kurs_malumot[T]
        ro_yxat_btn = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(
                    text="✅ Ro'yxatdan o'tish",
                    url='https://t.me/+998915093298'
                )]
            ]
        )
        await msg.answer(
            f"{info['nomi']}\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            f"{info['tavsif']}",
            reply_markup=ro_yxat_btn
        )


@dp.message(F.text.in_(mentorlar_list))
async def mentor_handler(msg: Message):
    T = msg.text

    if T == mentorlar_list[8]:  # Orqaga
        await msg.answer("🏠 Bosh menyu", reply_markup=Menu)
        return

    if T in mentor_malumot:
        bog_lanish_btn = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(
                    text="💬 Mentor bilan bog'lanish",
                    url='https://t.me/+998915093298'
                )]
            ]
        )
        await msg.answer(mentor_malumot[T], reply_markup=bog_lanish_btn)


@dp.message()
async def message_handler(msg: Message):
    T = msg.text.lower() if msg.text else ""
    if T in ('seni kim yaratgan', 'seni kim yasagan'):
        await msg.answer('🧑‍💻 Meni Asadbek yaratgan!')
    else:
        await msg.answer(
            "❓ Kechirasiz, tushunmadim.\n"
            "Iltimos, quyidagi menyudan foydalaning 👇",
            reply_markup=Menu
        )


# ───────────────────────────────────────────────
# MAIN
# ───────────────────────────────────────────────
async def main():
    bot = Bot(token=API)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())