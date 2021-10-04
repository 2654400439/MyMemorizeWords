import numpy as np
from playsound2 import playsound
# playsound("D:\python_project\MyMemorizeWords\Speech_US\crucible.mp3")
a = np.array([[1,2],[3,3]])
a = np.concatenate((a,[[7,9]]),axis=0)
print(a)
