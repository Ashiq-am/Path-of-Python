def filter_even_numbers(data):
    for value in data:
        if value % 2 == 0:
            yield value


my_data = [1, 2, 3, 4, 5]
result_generator = filter_even_numbers(my_data)

for value in result_generator:
    print(value)
