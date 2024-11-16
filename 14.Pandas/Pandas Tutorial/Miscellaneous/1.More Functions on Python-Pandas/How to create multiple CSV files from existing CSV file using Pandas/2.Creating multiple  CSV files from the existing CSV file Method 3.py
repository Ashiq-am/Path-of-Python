for (gender), group in data['Spending Score'].groupby(data['Gender']):
    group.to_csv(f'{gender}Score.csv', index=False)

print(pd.read_csv("MaleScore.csv"))
print(pd.read_csv("FemaleScore.csv"))
