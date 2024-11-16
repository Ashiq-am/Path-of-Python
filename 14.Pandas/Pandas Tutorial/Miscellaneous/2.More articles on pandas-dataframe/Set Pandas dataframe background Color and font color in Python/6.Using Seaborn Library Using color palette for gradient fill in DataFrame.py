# Import seaborn library
import seaborn as sns

# Declaring the cm variable by the
# color palette from seaborn
cm = sns.light_palette("green", as_cmap=True)

# Visualizing the DataFrame with set precision
print("\nModified Stlying DataFrame:")
df.style.background_gradient(cmap=cm).set_precision(2)
