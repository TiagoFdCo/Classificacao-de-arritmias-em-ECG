# importing the libraries for DSP and plotting
import wfdb
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal

#reading a signal
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

# time axis in seconds
t = np.arange(ecg.size) / fs

# plot raw vs filtered
fig, ax = plt.subplots()
ax.plot(t, ecg,      linewidth=1.0, color='blue', label='original ECG')
ax.plot(t, ecg_filt, linewidth=1.0, color='red',  label='filtered ECG')

plt.xlabel('time (s)')
plt.ylabel('amplitude (mV)')
plt.xlim([50, 55])                    # 5-second window. Changeable 
plt.legend()
plt.show()

#filtering - derivative step

derivative_signal = np.diff(ecg_filt)
t2 = np.arange(derivative_signal.size) / fs

#plotting
fig2, ax = plt.subplots()
ax.plot(t2, derivative_signal,      linewidth=1.0, color='blue', label='differentiated ECG signal')
plt.xlabel('time (s)')
plt.ylabel('amplitude (mV)')
plt.xlim([50, 55])                    # 5-second window. Changeable 
plt.legend()
plt.show()

#squaring the signal

squared_signal = derivative_signal**2
t3 = np.arange(squared_signal.size) / fs


#plotting
fig3, ax = plt.subplots()
ax.plot(t3, squared_signal,      linewidth=1.0, color='blue', label='squared ECG signal')
plt.xlabel('time (s)')
plt.ylabel('amplitude (mV)')
plt.xlim([50, 55])                    # 5-second window. Changeable 
plt.legend()
plt.show()

#moving window integration
# tamanho da janela: ~150 ms convertidos para amostras
window_size = int(0.150 * fs)          # 54 amostras para fs=360

# kernel de uns, normalizado (média móvel)
window = np.ones(window_size) / window_size

# integração = convolução com o kernel
integrated_signal = np.convolve(squared_signal, window, mode='same')

# eixo de tempo
t4 = np.arange(integrated_signal.size) / fs

# plot
fig4, ax = plt.subplots()
ax.plot(t4, integrated_signal, linewidth=1.0, color='green', label='integrated ECG signal')
plt.xlim([50, 55])
plt.legend()
plt.show()


#improving algorithm to short function
def pan_thompkins(ecg_filt, fs):
    abc = 'abc'