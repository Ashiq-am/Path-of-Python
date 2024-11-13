# Import required modules
from fitness_tools.meals.meal_maker import MakeMeal

# Create object
obj = MakeMeal(160, goal='weight_gain', activity_level='moderate',
			body_type='mesomorph')

# Call required method
obj.daily_requirements()
