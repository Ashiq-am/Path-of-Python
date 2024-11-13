import re
testData = "This, is - underscored _ example?!"
print(re.findall(r"[\w']+", testData))
