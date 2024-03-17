from aiogram import Router, flags, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command


import app.keyboards as kb

router = Router()

# Реакция на команду старт
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!\nЯ - *TamaBot*. Тамагочи в твоем Телеграм.\nСоздаем нового питомца?',
                         reply_markup=kb.main)

### MAIN HANDLERS

@router.message(Command('show'))
async def show_pet(message: Message):
    await message.reply_animation(animation='CgACAgIAAxkBAAMdZfbfLpMUqh0MSL4smTPSrSAjJWsAAg9JAAKTsqBL0PKobZYBOfY0BA')
    

# Обработчик ID фотографий
@router.message(F.animation)
async def check_photo_id(message: Message):
    await message.answer(f'ID фото: {message.animation.file_id}')

# Callback на ответ Yes
@router.callback_query(F.data == 'answer-yes')
async def creation(callback: CallbackQuery):
    await callback.answer('Вы выбрали: Да!')
    await callback.message.edit_text('Отлично!\nКого вы хотите создать?', reply_markup=kb.animals)

# Callback на выбор кошки
@router.callback_query(F.data == 'cat')
async def creation(callback: CallbackQuery):
    # await callback.answer('Вы выбрали: Да!')
    await callback.message.reply_animation(animation='CgACAgIAAxkBAAMdZfbfLpMUqh0MSL4smTPSrSAjJWsAAg9JAAKTsqBL0PKobZYBOfY0BA',
                                           reply_markup=kb.animals_choice)

# # Callback на выбор кошки
# @router.callback_query(F.data == 'cat')
# async def creation(callback: CallbackQuery):
#     # await callback.answer('Вы выбрали: Да!')
#     await callback.message.edit_media(media='')
