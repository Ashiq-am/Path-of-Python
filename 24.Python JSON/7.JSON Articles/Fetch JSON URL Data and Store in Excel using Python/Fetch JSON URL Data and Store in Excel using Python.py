import requests
import pandas as pd

# Step 1: Define the URL for the JSON data
url = 'https://jsonplaceholder.typicode.com/todos'

# Step 2: Fetch the JSON data
response = requests.get(url)

# Step 3: Check if the request was successful
if response.status_code == 200:
    json_data = response.json()

    # Step 4: Convert JSON data to a DataFrame
    df = pd.DataFrame(json_data)

    # Step 5: Save the DataFrame to an Excel file
    excel_file = 'todos.xlsx'
    df.to_excel(excel_file, index=False, sheet_name='Todos')

    print(f"Data has been successfully saved to {excel_file}")
else:
    print(f"Failed to fetch data. HTTP Status code: {response.status_code}")
