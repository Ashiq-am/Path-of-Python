# Get price for a particular weight
def change_price(weight_value):

	g_price = float(weight_value)*get_number_from_string(gold_price())
	s_price = float(weight_value)*get_number_from_string(silver_price())

	silver_price_label.config(text=f"{s_price} Rs")
	gold_price_label.config(text=f"{g_price} Rs")
