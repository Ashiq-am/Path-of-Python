df_val = pd.read_csv('..../C-NMC_Leukemia/validation_data/C-NMC_test_prelim_phase_data_labels.csv')
# Drop Patient_ID column and rename columns
df_val['image_paths'] = df_val['new_names']
df_val['image_labels'] = df_val['labels']
df_val = df_val[['image_paths', 'image_labels']]

base_path = '..../C-NMC_Leukemia/validation_data/C-NMC_test_prelim_phase_data'
df_val['image_paths'] = df_val['image_paths'].apply(lambda x: os.path.join(base_path, x))
