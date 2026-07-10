import wfdb
from src.preprocessing.pan_tompkins import pan_tompkins
from src.visualization import plot_pan_tompkins_stages

record = wfdb.rdrecord('data/mit-bih-arrhythmia-database-1.0.0/101')
ecg, fs = record.p_signal[:, 0], record.fs

peaks, stages = pan_tompkins(ecg, fs, return_stages=True)   # processa
plot_pan_tompkins_stages(stages, fs, peaks=peaks)           # desenha

fig = plot_pan_tompkins_stages(stages, fs, peaks=peaks)
fig.savefig('results/pan_tompkins_stages.png', dpi=150, bbox_inches='tight')