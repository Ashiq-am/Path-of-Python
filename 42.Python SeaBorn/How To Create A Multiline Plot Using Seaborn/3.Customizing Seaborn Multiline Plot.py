import seaborn as sns
import matplotlib.pyplot as plt
data = sns.load_dataset('fmri')
sns.lineplot(data=data, x='timepoint', y='signal', hue='region', ci=None)

# Customize plot appearance
plt.xlabel('Timepoint', fontsize=14, fontweight='bold', color='blue')  # Set x-axis label with custom font properties
plt.ylabel('Signal Intensity', fontsize=14, fontweight='bold', color='blue')  # Set y-axis label with custom font properties
plt.title('FMRI Signal Over Time by Region', fontsize=16, fontweight='bold', color='green')  # Set plot title with custom font properties

# Customize legend
plt.legend(title='Brain Region', title_fontsize='12', loc='upper left')  # Customize legend title and position

# Customize grid
plt.grid(True, linestyle='--', alpha=0.5, color='gray')  # Enable grid with custom linestyle, transparency, and color
plt.show()
