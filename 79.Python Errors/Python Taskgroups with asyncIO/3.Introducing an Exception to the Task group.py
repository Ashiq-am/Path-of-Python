async def divide(num1,num2):
	if num2 == 0:
		raise Exception("Trying to Divide by Zero")
	else:
		print(num1/num2)


async def main():
	async with asyncio.TaskGroup() as task_group:
		task_group.create_task(square_number(5))
		task_group.create_task(square_root(25))
		task_group.create_task(square_root(18))

		# Returns Exception
		task_group.create_task(square_number("Geeks"))
		task_group.create_task(square_number('a'))
		task_group.create_task(divide(10,0))
