# import numpy
import numpy as np

# using numpy.core.fromarrays() method
li1 = np.array([101, 102, 103, 104])
li2 = np.array(['Jitender', 'Purnima', 'Ruhi', 'Varun'])
li3 = np.array([21, 22, 12, 35])

gfg = np.core.records.fromarrays([li1, li2, li3],
					names ='Rollno, Name, Age')

print(gfg.Rollno)
print(gfg.Name)
print(gfg.Age)
