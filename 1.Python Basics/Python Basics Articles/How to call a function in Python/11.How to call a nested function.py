def outer_funtion():
  print("This is outer function.")
  def inner_function():
    print("And this is inner function.")
  inner_function()

outer_function()
