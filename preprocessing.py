#importing the libraries for DSP and plotting
import wfdb
import pandas as pd
import matplotlib.pyplot as plt #optional, wfdb already have a plotting method
import numpy as np
import scipy as sp
import scipy.signal


#native file reading method
signal = wfdb.rdrecord('data/mit-bih-arrhythmia-database-1.0.0/mit-bih-arrhythmia-database-1.0.0/101')

#plotting
wfdb.plot_wfdb(record=signal, title='Record 100')
