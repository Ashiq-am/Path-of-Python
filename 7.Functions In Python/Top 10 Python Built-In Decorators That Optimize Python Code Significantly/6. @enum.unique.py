from enum import Enum, unique

@unique
class Days(Enum):
	MONDAY = 1
	TUESDAY = 2
	WEDNESDAY = 3
	THURSDAY = 2 # ValueError: duplicate values found in <enum 'Days'>: THURSDAY -> TUESDAY
