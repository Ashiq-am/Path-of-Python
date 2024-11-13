if select == "Histogram":
    fig = px.bar(sentiment, x='Sentiment', y='Tweets',
                 color='Tweets', height=500)
    st.plotly_chart(fig)
else:
    fig = px.pie(sentiment, values='Tweets', names='Sentiment')
    st.plotly_chart(fig)

st.sidebar.markdown('Time & Location of tweets')
hr = st.sidebar.slider("Hour of the day", 0, 23)
data['Date'] = pd.to_datetime(data['tweet_created'])
hr_data = data[data['Date'].dt.hour == hr]
if not st.sidebar.checkbox("Hide", True, key='2'):
    st.markdown("### Location of the tweets based on the hour of the day")
    st.markdown("%i tweets during %i:00 and %i:00" %
                (len(hr_data), hr, (hr+1) % 24))
    st.map(hr_data)
