# import the necessary libraries
import sweetviz as sv
from sklearn.datasets import load_breast_cancer

# Load the dataset
cancer = load_breast_cancer(as_frame=True)
# dataframe
df = cancer.frame

# Define the FeatureConfig object to force
# the target feature to be numerical
my_feature_config = sv.FeatureConfig(force_num=['target'])

# Create a boolean array to use as the grouping condition
condition_series = df['target'] == 0

# Analyze the dataset with the specified FeatureConfig object
# and grouping condition
my_report = sv.compare_intra(df,
							condition_series,
							['malignant', 'benign'],
							feat_cfg=my_feature_config,
							target_feat='target')

# Generate and display the report
my_report.show_html()
