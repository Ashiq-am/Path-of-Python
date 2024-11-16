pos_list = []
neg_list = []
neu_list = []
for i in tweets["date"].unique():
	temp = tweets[tweets["date"] == i]
	positive_temp = temp[temp["sentiment"] == "positive"]
	negative_temp = temp[temp["sentiment"] == "negative"]
	neutral_temp = temp[temp["sentiment"] == "neutral"]
	pos_list.append(((positive_temp.shape[0]/temp.shape[0])*100, i))
	neg_list.append(((negative_temp.shape[0]/temp.shape[0])*100, i))
	neu_list.append(((neutral_temp.shape[0]/temp.shape[0])*100, i))

neu_list = sorted(neu_list, key=lambda x: x[1])
pos_list = sorted(pos_list, key=lambda x: x[1])
neg_list = sorted(neg_list, key=lambda x: x[1])

x_cord_neg = []
y_cord_neg = []

x_cord_pos = []
y_cord_pos = []

x_cord_neu = []
y_cord_neu = []

for i in neg_list:
	x_cord_neg.append(i[0])
	y_cord_neg.append(i[1])


for i in pos_list:
	x_cord_pos.append(i[0])
	y_cord_pos.append(i[1])

for i in neu_list:
	x_cord_neu.append(i[0])
	y_cord_neu.append(i[1])


plt.figure(figsize=(16, 9),
		dpi=600) # Push new figure on stack
plt.plot(y_cord_neg, x_cord_neg, label="negative",
		color="red")
plt.plot(y_cord_pos, x_cord_pos, label="positive",
		color="green")
plt.plot(y_cord_neu, x_cord_neu, label="neutral",
		color="blue")
plt.xticks(np.arange(0, len(tweets["date"].unique()) + 1, 5))
plt.xticks(rotation=90)
plt.grid(axis='x')

plt.legend()
