def load_data(file_path):
    return pd.read_csv(file_path)

def clean_data(df):
    df.dropna(inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    return df

# Usage
sales_data = load_data('sales_data.csv')
cleaned_sales_data = clean_data(sales_data)
