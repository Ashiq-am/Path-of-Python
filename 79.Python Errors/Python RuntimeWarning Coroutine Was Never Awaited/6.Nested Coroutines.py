async def outer_coroutine():
	await inner_coroutine()

async def inner_coroutine():
	print("Nested coroutine")

await outer_coroutine()