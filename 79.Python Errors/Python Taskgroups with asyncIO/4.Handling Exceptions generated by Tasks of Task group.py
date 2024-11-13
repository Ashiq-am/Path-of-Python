async def main():
    try:
        async with asyncio.TaskGroup() as task_group:
            task_group.create_task(square_number(5))
            task_group.create_task(square_root(25))
            task_group.create_task(square_root(18))

            # Returns Exception
            task_group.create_task(square_number("Geeks"))
            task_group.create_task(square_number('a'))
            task_group.create_task(divide(10, 0))
    except* TypeError as te:
        for errors in te.exceptions:
            print(errors)
    except* Exception as ex:
        print(ex.exceptions)

    print("All different tasks of task_group has \
    executed successfully!!")

    asyncio.run(main())
