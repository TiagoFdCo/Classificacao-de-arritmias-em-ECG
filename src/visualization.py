import numpy as np
import matplotlib.pyplot as plt

def plot_pan_tompkins_stages(stages, fs, window=(50, 55), peaks=None):
    """
    stages : dict com 'filtered', 'derivative', 'squared', 'integrated'
    fs     : frequência de amostragem (Hz)
    window : (t_ini, t_fim) em segundos
    peaks  : índices dos picos detectados (opcional)
    """
    t = np.arange(len(stages['filtered'])) / fs
    fig, axes = plt.subplots(len(stages), 1, figsize=(11, 8), sharex=True)

    for ax, (nome, sinal) in zip(axes, stages.items()):
        ax.plot(t, sinal, linewidth=1.0, label=nome)
        ax.legend(loc='upper right')

    if peaks is not None:
        axes[-1].plot(peaks / fs, stages['integrated'][peaks], 'kx')

    axes[-1].set_xlim(window)
    axes[-1].set_xlabel('tempo (s)')
    fig.tight_layout()
    return fig            # ← devolve, não mostra