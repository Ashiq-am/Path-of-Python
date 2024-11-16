all_categories = set(cat for sublist in df['Categories'] for cat in sublist)
print(all_categories)
