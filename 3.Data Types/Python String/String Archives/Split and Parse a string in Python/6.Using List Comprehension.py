# Given input string
Text = "Mango,Orange,Banana"
# Split the input string by commas and filter out empty parts using list comprehension
P = [part for part in Text.split(',') if part.strip()]
# print
print(P)
