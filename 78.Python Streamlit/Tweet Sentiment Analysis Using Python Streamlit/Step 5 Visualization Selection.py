select = st.sidebar.selectbox('Visualisation of Tweets', [
                              'Histogram', 'Pie Chart'], key=1)
sentiment = data['airline_sentiment'].value_counts()
sentiment = pd.DataFrame(
    {'Sentiment': sentiment.index, 'Tweets': sentiment.values})
