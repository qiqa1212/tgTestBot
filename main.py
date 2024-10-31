from aiogram import Bot, Dispatcher, executor, types

bot = Bot('7775230802:AAF-xnz7AGINcZh-0pDktmRXf0jl0tb4vgA')
dp = Dispatcher(bot)


@dp.message_handler(compands=['start'])
async def start(message:  types.Message):
   await message.answer('Hello')

executor.start_polling(dp)