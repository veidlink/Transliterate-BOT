import logging 
import os
from aiogram import Bot, Dispatcher, executor, types 
from dotenv import load_dotenv 

load_dotenv('.env')
TOKEN = os.environ.get('TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot) 

transliteration_dict = {
    ' ': ' ',
    '-':'-',
    '--':'--'
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'E',
    'Ж': 'ZH',
    'З': 'Z',
    'И': 'I',
    'Й': 'I',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'KH',
    'Ц': 'TS',
    'Ч': 'CH',
    'Ш': 'SH',
    'Щ': 'SHCH',
    'Ы': 'Y',
    'Ъ': 'IE',
    'Э': 'E',
    'Ю': 'IU',
    'Я': 'IA'
}


@dp.message_handler(commands=['start']) 
async def send_welcome(message: types.Message):
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    text = f'Присылай текст кириллицей, {user_name}, разберемся!'

    logging.info(f'{user_name} {user_id} sent message:{message.text}')    
    await message.reply(text)
    

@dp.message_handler()
async def send_transliterate(message: types.Message):
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    
    text = str(message.text).upper()
    text = ''.join([transliteration_dict[i] for i in text])

    logging.info(f'{user_name} {user_id} sent message:{text}')    
    await bot.send_message(user_id, text)

if __name__ == '__main__':
    executor.start_polling(dp)