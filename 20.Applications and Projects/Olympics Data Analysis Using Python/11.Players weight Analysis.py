MenOverTime = merged[(merged.Sex == 'M') &
					(merged.Season == 'Summer')]
wlMenOverTime = MenOverTime.loc[MenOverTime['Sport'] == 'Weightlifting']

plt.figure(figsize=(20, 10))
sns.pointplot('Year', 'Weight', data=wlMenOverTime, palette='Set2')
plt.title('Weight over year for Male Lifters')
plt.show()
