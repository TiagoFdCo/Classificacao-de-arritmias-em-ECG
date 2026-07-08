# importing the libraries for DSP and plotting
import wfdb
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal

record = wfdb.rdrecord('data/mit-bih-arrhythmia-database-1.0.0/mit-bih-arrhythmia-database-1.0.0/101')

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

#moving window integration
# tamanho da janela: ~150 ms convertidos para amostras
window_size = int(0.150 * fs)          # 54 amostras para fs=360

# kernel de uns, normalizado (média móvel)
window = np.ones(window_size) / window_size

#improving algorithm to short function
def pan_thompkins(ecg_filt, fs):
    diff = np.diff(ecg_filt)
    squared = diff ** 2
    integrated = np.convolve(squared, window, mode='same')

    #plotting only
    t1 = np.arange(ecg_filt.size) / fs
    t2 = np.arange(diff.size) / fs
    t3 = np.arange(squared.size) / fs
    t4 = np.arange(integrated.size) / fs
    fig1, ax = plt.subplots()
    ax.plot(t1, ecg_filt, linewidth=1.0, color='green', label='pass-band filtered ECG signal')
    plt.xlim([50, 55])
    plt.legend()
    plt.show()
    fig2, ax = plt.subplots()
    ax.plot(t2, diff, linewidth=1.0, color='red', label='differentiated ECG signal')
    plt.xlim([50, 55])
    plt.legend()
    plt.show()
    fig3, ax = plt.subplots()
    ax.plot(t3, squared, linewidth=1.0, color='blue', label='squared ECG signal')
    plt.xlim([50, 55])
    plt.legend()
    plt.show()
    fig4, ax = plt.subplots()
    ax.plot(t4, integrated, linewidth=1.0, color='purple', label='integrated ECG signal')
    plt.xlim([50, 55])
    plt.legend()
    plt.show()

    return integrated


pan_thompkins(ecg_filt, fs)

