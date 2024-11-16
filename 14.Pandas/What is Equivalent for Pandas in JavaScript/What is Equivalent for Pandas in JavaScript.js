const { DataFrame } = require('pandas-js');

// Create a DataFrame
const data = {
    'Name': ['GFG1', 'GFG2', 'GFG3'],
    'Age': [25, 30, 35]
};
const df = new DataFrame(data);

// Filter rows where Age is greater than 30
const filtered_df = df.filter(df.get('Age').gt(30));

console.log(filtered_df.toString());
