# code
StatusCode = Literal[200, 404, 500]

def is_status_code(value) -> bool:
    return value in get_args(StatusCode)

print(is_status_code(200))
print(is_status_code(403))
