import aiohttp
async def fetch_data():
	async with aiohttp.ClientSession() as session:
		async with session.get('https://example.com') as response:
			return await response.text()
result = fetch_data()
