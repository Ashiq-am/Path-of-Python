# Plot Histogram
sns.histplot(data = penguins, x = "body_mass_g", kde = True, hue = "species")
