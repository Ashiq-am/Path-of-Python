@dp.message_handler(commands=['start'])
async def check(message: types.Message):
    await message.reply("hi! how are you", reply_markup=keyboard_inline)
