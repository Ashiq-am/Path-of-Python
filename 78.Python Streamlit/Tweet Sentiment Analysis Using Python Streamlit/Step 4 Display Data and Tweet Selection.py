if st.checkbox("Show Data"):
    st.write(data.head(50))

st.sidebar.subheader('Tweets Analyser')
tweets = st.sidebar.radio(
    'Sentiment Type', ('positive', 'negative', 'neutral'))
st.write(data.query('airline_sentiment==@tweets')
         [['text']].sample(1).iat[0, 0])
st.write(data.query('airline_sentiment==@tweets')
         [['text']].sample(1).iat[0, 0])
st.write(data.query('airline_sentiment==@tweets')
         [['text']].sample(1).iat[0, 0])
st.write(data.query('airline_sentiment==@tweets')
         [['text']].sample(1).iat[0, 0])
