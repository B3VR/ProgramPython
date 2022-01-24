import imp
from Signal import Signal
import numpy as np

samples = np.array([322, 324, 211])
signal = Signal("EKG1", 11.32, samples)
signal.toString()