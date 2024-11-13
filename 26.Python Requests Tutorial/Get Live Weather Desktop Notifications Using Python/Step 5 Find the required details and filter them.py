current_temp = soup.find_all("span",class_=" _-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY")
chances_rain = soup.find_all("div",class_= "_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf")

temp = (str(current_temp))
temp_rain = str(chances_rain)

result = "current_temp " + temp[128:-9] + " in patna bihar" + "\n" +temp_rain[131:-14]
