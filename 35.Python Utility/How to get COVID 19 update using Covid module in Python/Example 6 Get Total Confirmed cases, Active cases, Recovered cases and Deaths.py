from covid import Covid


covid = Covid()

confirmed = covid.get_total_confirmed_cases()
print('Confirmed :', end =" ")
print(confirmed)

active = covid.get_total_active_cases()
print("Active:", end =" ")
print(active)

recovered = covid.get_total_recovered()
print('Recovered:', end =" ")
print(recovered)

deaths = covid.get_total_deaths()
print('Deaths:', end =" ")
print(deaths)
