import pywhatkit as kit
try:
  pwk.search("Geeks for geeks")
except KeyError as e:
  print(f"KeyError occurred: {e}")
