@dp.message_handler()
async def check_rp(message: types.Message):
    if message.text == '_button1':
        await message.reply("Hi! this is first reply keyboards button.")

    elif message.text == '_button2':
        await message.reply("Hi! this is second reply keyboards button.")

    else:
        await message.reply(f"Your message is: {message.text}")
