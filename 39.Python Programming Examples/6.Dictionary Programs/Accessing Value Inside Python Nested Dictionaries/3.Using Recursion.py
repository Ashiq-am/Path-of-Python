# Using a recursive function
market = {"fruits": {"apple": 10, "orange": 40, "strawberry": 30, "grapes": 200},
          "vegetables": {"carrot": 50, "beans": 100, "tomato": 70}}


def get_nested_value(dictionary, keys):
    if not keys:
        return dictionary
    return get_nested_value(dictionary.get(keys[0], {}), keys[1:])


# Example usage
beans_quantity = get_nested_value(market, ['vegetables', 'beans'])
print("Beans Quantity:", beans_quantity)  # Output: 100