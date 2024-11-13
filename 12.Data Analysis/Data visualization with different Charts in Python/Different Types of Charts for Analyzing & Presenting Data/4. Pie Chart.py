plt.pie(df['Age'], labels={"A", "B", "C",
                           "D", "E", "F",
                           "G", "H", "I", "J"},

        autopct='% 1.1f %%', shadow=True)
plt.show()

plt.pie(df['Income'], labels={"A", "B", "C",
                              "D", "E", "F",
                              "G", "H", "I", "J"},

        autopct='% 1.1f %%', shadow=True)
plt.show()

plt.pie(df['Sales'], labels={"A", "B", "C",
                             "D", "E", "F",
                             "G", "H", "I", "J"},
        autopct='% 1.1f %%', shadow=True)
plt.show()
