# checking datatype
print(type(data.AdmissionDate[0]))

# convert to date
data['AdmissionDate'] = pd.to_datetime(data['AdmissionDate'])

# verify datatype
print(type(data.AdmissionDate[0]))
