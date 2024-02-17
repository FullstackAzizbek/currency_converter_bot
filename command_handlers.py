from aiogram.types import BotCommand, Message
from aiogram.filters import CommandStart, Command
from aiogram import Router, F
from aiogram.utils.markdown import hbold
import requests
from config import API_TOKEN

command_router = Router()
api_router = Router()
message_router = Router()


@command_router.message(CommandStart())
async def start_handler(message: Message):
    s = f"Assalomu Alaykum! {hbold(message.from_user.full_name)}\n"
    t = "Bu bot orqali siz doimiy valyuta kurslari narxlarini bilishingiz mumkin!"
    await message.answer(s)
    await message.answer(t)


@command_router.message(Command('help' ,prefix='!#/'))
async def help_handler(message:Message):
    s = "Iltimos kerakli valyutani tanlang:\n\n\n"
    s += "\t- RUBL kursini bilish uchun /rub ni bosing\n\n"
    s += "\t- USD kursini bilish uchun /usd ni bosing\n\n"
    s += "\t- EURO kursini bilish uchun /eur ni bosing\n\n"
    s += "\nKerakli valyutani tanlang va uning so'mga nisbatan qiymatini bilib oling."
    await message.reply(text=s)


# Define global variables with initial value None

l = ['RUB', 'EUR', 'USD']

@api_router.message(Command('all', prefix='!#/'))
async def api_handler(message: Message):
    global l
    
    response = requests.get(API_TOKEN)
    result = response.json()
    s = 'Kurslar: \n\n'
    for currency in result:
        if currency['Ccy'] in l:
            s += f"1 {currency['CcyNm_UZ']} = {currency['Rate']} sumga teng.\n"
    await message.reply(text=s)

@message_router.message(Command('usd', prefix='!#/'))
async def usd_handler(message: Message):
    res = requests.get(API_TOKEN)
    result = res.json()

    s = ''
    for currency in result:
        if currency['Ccy'] == 'USD':
            s += f"1 USD - {currency['Rate']} so'm"
    
    await message.reply(text=s)
@message_router.message(Command('eur',prefix='!#/'))
async def usd_handler(message: Message):
    res = requests.get(API_TOKEN)
    result = res.json()
    s = ''
    for currency in result:
        if currency['Ccy'] == 'EUR':
            s += f"1 EURO - {currency['Rate']} so'm"
    
    await message.reply(text=s)
@message_router.message(Command('rub', prefix='!#/'))
async def usd_handler(message: Message):
    res = requests.get(API_TOKEN)
    result = res.json()
    s = ''
    for currency in result:
        if currency['Ccy'] == 'RUB':
            s += f"1 RUBLE - {currency['Rate']} so'm"
    
    await message.reply(text=s)

@message_router.message(F.text.isdigit())
async def converter(message: Message):
    x = int(message.text)
    res = requests.get(API_TOKEN)
    result = res.json()
    # Check if result is None
    if result is None:
        await message.reply("Kechirasiz, ma'lumotlar yuklanmagan. Iltimos, oldin /all buyrug'ini ishga tushiring.")
        return
    
    s = f"{x} so'm:\n\n "
    for currency in result:
        if currency['Ccy'] in l:
            s += f"{x / float(currency['Rate']) :.2f} {currency['CcyNm_UZ']}ga teng.\n\n"
    await message.reply(s)

