from werkzeug.datastructures import ImmutableMultiDict

# In this example we are adding gadget and accessories
d = ImmutableMultiDict([('Gadget', 'DSLR'),
						('Accessories','Lens 18-105mm'),
						('Accessories', 'Lens 70-200mm'),
						('Accessories', 'Tripod stand')])
list(d.lists())
