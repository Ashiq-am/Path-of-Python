market = {"fruits": {"apple": 10, "orange": 40, "strawberry": 30, "grapes": 200},
          "vegetables": {"carrot": 50, "beans": 100, "tomato": 70}}
# Printing the value using get() method of dictionary by passing key

print("Orange Price:", market.get("fruits").get("orange"))
print("Grapes Price:", market.get("fruits").get("grapes"))
print("Tomato Price:", market.get("vegetables").get("tomato"))