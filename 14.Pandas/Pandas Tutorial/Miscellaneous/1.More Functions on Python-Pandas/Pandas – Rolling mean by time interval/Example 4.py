# importing matplotlib module
import matplotlib.pyplot as plt
plt.style.use('default')

# %matplotlib inline: only draw static
# images in the notebook
#%matplotlib inline

tesla_df[['Close', 'MA30', 'MA200']].plot(
label='tesla', figsize=(16, 8))
