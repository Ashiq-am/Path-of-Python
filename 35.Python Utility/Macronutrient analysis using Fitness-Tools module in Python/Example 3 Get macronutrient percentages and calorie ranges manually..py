# Import required module
from fitness_tools.meals.meal_maker import MakeMeal

# Create object
obj = MakeMeal(160, min_cal=10, max_cal=15, fat_percent=0.1,
			protein_percent=0.75, carb_percent=0.15)

# returns calories, fat, protein,
# and carbs in grams for one day
obj.daily_requirements()
