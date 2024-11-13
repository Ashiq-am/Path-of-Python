import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
sns.set_context('poster', font_scale = 2)
sns.countplot(x ='sex', data = tips, palette ='coolwarm')
