# importing the libraries for DSP and plotting
import wfdb
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal

# native file reading method
record = wfdb.rdrecord('data/mit-bih-arrhythmia-database-1.0.0/mit-bih-arrhythmia-database-1.0.0/101')
wfdb.plot_wfdb(record=record)

# extract one channel as a 1D array
ecg = record.p_signal[:, 0]          # channel 0 (check record.sig_name to confirm it's MLII)
fs  = record.fs                       # 360 Hz for MIT-BIH

# filtering — bandpass 0.5–40 Hz
hpf_cutoff = 0.5                      # high-pass edge: kills baseline wander below this
lpf_cutoff = 40                       # low-pass edge: kills muscle/mains noise above this

sos = scipy.signal.butter(10,
                          [hpf_cutoff, lpf_cutoff],   # [low, high] in ascending order
                          btype='bp',
                          analog=False,
                          output='sos',
                          fs=fs)

# apply with zero phase shift (forward-backward)
ecg_filt = scipy.signal.sosfiltfilt(sos, ecg)
