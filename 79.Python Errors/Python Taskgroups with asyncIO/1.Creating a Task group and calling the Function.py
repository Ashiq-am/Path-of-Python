# Defining main function
async def main():
	async with asyncio.TaskGroup() as task_group:
		# Calling square number function
		task_group.create_task(square_number(5))
		task_group.create_task(square_number(10))

# calling main function
asyncio.run(main())
