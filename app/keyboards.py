from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Да!', callback_data='answer-yes')],
    [InlineKeyboardButton(text='Нет :(', callback_data='answer-no'),]
])

animals = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Cat', callback_data='cat')],
    [InlineKeyboardButton(text='Dog(недоступно)', callback_data='dog'),]
])

animals_choice = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Выбрать', callback_data='choose')],
    [InlineKeyboardButton(text='Далее(недоступно)', callback_data='next-animal'),]
])