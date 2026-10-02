"""
Funções auxiliares para processamento de sinais
Atividade de laboratório - Karplus-Strong e Reconstrução de Sinais
"""

import numpy as np
import matplotlib.pyplot as plt


def create_sine_signal(f=440.0, dur=1.0, fs=48e3):
    '''
    Cria um sinal oscilatório (senoide) puro.

    Parâmetros:
    -----------
    f  : float
        Frequência do sinal em Hz (altura da nota)
    dur: float
        Duração do sinal em segundos
    fs : float
        Taxa de amostragem em Hz (amostras por segundo)

    Retorna:
    --------
    x  : ndarray
        Vetor de amostras do sinal
    fs : float
        Taxa de amostragem (retornada para uso em play/plot)

    Fórmula:
    --------
    x[n] = sin(ω₀·n) onde ω₀ = 2π·f/fs

    Exemplo:
    --------
    >>> x, fs = create_sine_signal(f=440, dur=1.0, fs=44100)
    >>> # x tem 44100 amostras (1 segundo a 44.1 kHz)
    '''

    N  = int(dur * fs)              # Número de amostras: N = d·fs
    n  = np.arange(N)               # Vetor de índices [0, 1, 2, ..., N-1]
    w0 = 2 * np.pi * f / fs         # Frequência digital: ω₀ = 2π·f/fs

    x = np.sin(w0 * n)              # Senoide

    return x, fs


def create_random_sine_signal(dur=1.0):
    '''
    Cria um sinal senoide puro com frequência e taxa de amostragem aleatórias.

    Esta função é útil para testes e exercícios onde é preciso gerar
    sinais com parâmetros variados.

    Parâmetros:
    -----------
    dur : float
        Duração do sinal em segundos (padrão: 1.0)

    Retorna:
    --------
    x   : ndarray
        Vetor de amostras do sinal
    t   : ndarray
        Vetor de tempo (segundos) correspondente a cada amostra
    fs  : float
        Taxa de amostragem (aleatória)
    f   : float
        Frequência do sinal em Hz (aleatória)

    Exemplo:
    --------
    >>> x, t, fs, f = create_random_sine_signal(dur=1.5)
    >>> print(f'Frequência: {f:.2f} Hz, fs={fs} Hz')
    >>> # Plotar os primeiros 20 ms
    >>> r = int(0.02 * fs)
    >>> plt.plot(t[:r], x[:r])
    '''

    # Gerar valores aleatórios
    f = np.random.uniform(100, 1000)                      # frequência entre 100 e 1000 Hz
    fs = np.random.choice([22050, 44100, 48000, 96000])  # fs aleatória

    # Criar o sinal usando create_sine_signal
    x, _ = create_sine_signal(f, dur, fs)

    # Criar eixo de tempo
    n = np.arange(len(x))
    t = n / fs

    return x, t, fs, f


if __name__ == "__main__":
    # Exemplo de uso
    print("=== Teste 1: Senoide pura ===")
    x1, fs1 = create_sine_signal(f=440, dur=1.0, fs=44100)
    print(f"Tamanho: {len(x1)} amostras")
    print(f"Taxa de amostragem: {fs1} Hz")
    print(f"Duração: {len(x1)/fs1:.2f} segundos\n")

    print("=== Teste 2: Senoide aleatória ===")
    x2, t2, fs2, f2 = create_random_sine_signal(dur=1.5)
    print(f"Frequência: {f2:.2f} Hz")
    print(f"Taxa de amostragem: {fs2} Hz")
    print(f"Tamanho: {len(x2)} amostras")
