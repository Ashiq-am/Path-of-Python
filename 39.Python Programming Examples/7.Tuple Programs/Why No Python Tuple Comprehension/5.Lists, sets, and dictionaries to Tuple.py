tuple_from_list_comprehension = tuple([x * 2 for x in range(5)])
tuple_from_set_comprehension = tuple({x+2 for x in range(5)})
tuple_from_dict_comprehension = tuple({
    idx: value for idx, value in enumerate(tuple_from_list_comprehension)
  })

print('tuple_from_list_comprehension:', tuple_from_list_comprehension)
print('tuple_from_set_comprehension:', tuple_from_set_comprehension)
print('tuple_from_dict_comprehension:', tuple_from_dict_comprehension)