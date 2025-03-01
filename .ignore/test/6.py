import pickle
import numpy as np
import unicodeit
from matplotlib import pyplot as plt

print(unicodeit.replace('dV^2/d^2t'))
a = 'dV²/d²t'
b = a.replace('²', '^2')
print(b)