class CustomDataset(Dataset):
    def __init__(self, csv_file, transform=None):
        self.data = pd.read_csv(csv_file)
        self.transform = transform

        # Handle missing values
        imputer = SimpleImputer(strategy='mean')
        self.data.fillna(self.data.mean(), inplace=True)

        # Encode categorical variables
        label_encoders = {}
        for column in self.data.select_dtypes(include=['object']).columns:
            label_encoders[column] = LabelEncoder()
            self.data[column] = label_encoders[column].fit_transform(self.data[column])

        # Scale numerical features
        scaler = StandardScaler()
        self.data[self.data.select_dtypes(include=['number']).columns] = scaler.fit_transform(
            self.data[self.data.select_dtypes(include=['number']).columns])

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        sample = torch.tensor(self.data.iloc[idx, :-1], dtype=torch.float)
        target = torch.tensor(self.data.iloc[idx, -1], dtype=torch.long)

        if self.transform:
            sample = self.transform(sample)

        return sample, target