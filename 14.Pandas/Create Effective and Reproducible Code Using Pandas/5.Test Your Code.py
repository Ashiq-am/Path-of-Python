def test_load_data():
    df = load_data('sales_data.csv')
    assert not df.empty, "Dataframe should not be empty"

def test_clean_data():
    df = pd.DataFrame({'date': ['2021-01-01', None]})
    cleaned_df = clean_data(df)
    assert cleaned_df['date'].isnull().sum() == 0, "There should be no missing dates after cleaning"
