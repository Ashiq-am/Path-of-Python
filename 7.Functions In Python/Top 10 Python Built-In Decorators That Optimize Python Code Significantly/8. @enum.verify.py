from enum import Enum, verify, UNIQUE, CONTINUOUS

@verify(UNIQUE)
class Days1(Enum):
	MONDAY = 1
	TUESDAY = 2
	WEDNESDAY = 3
	THURSDAY = 2 #ValueError: aliases found in <enum 'Days'>: THURSDAY -> TUESDAY

@verify(CONTINUOUS)
class Days2(Enum):
	MONDAY = 1
	TUESDAY = 2
	THURSDAY = 4 #ValueError: invalid enum 'Days': missing values 3
