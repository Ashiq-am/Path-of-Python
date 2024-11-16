from datetime import datetime, date

born='26/01/2000'
print("Born :",born)

#Identify given date as date month and year
born = datetime.strptime(born, "%d/%m/%Y").date()

#Get today's date
today = date.today()

print("Age :", today.year - born.year - ((today.month, today.day) < (born.month, born.day)))
