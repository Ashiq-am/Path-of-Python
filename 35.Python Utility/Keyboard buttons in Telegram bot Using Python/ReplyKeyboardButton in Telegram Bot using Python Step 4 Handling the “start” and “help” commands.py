@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hello! how are you?", reply_markup=keyboard_reply)
