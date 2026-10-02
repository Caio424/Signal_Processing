# Signal Processing - Atividade em Sala

Este repositório contém a **atividade de laboratório** realizada em sala de aula sobre **Processamento de Sinais Digitais**, com foco em:

- Criação de sinais digitais puros (senoides)
- Síntese de sinais periódicos e aleatórios
- Análise espectral usando Transformada Rápida de Fourier (FFT)
- Visualização de sinais no domínio do tempo e da frequência
- Fundamentos do **algoritmo Karplus-Strong** para síntese de áudio

## Objetivos da Atividade

A atividade foi estruturada em **desafios práticos** onde você deve:

1. ✅ **Completar funções** - Implementar funções de geração de sinais
2. ✅ **Responder perguntas com código** - Usar Python/NumPy para responder conceitos teóricos
3. ✅ **Plotar e analisar** - Visualizar sinais nos domínios do tempo e frequência
4. ✅ **Entender a relação** entre parâmetros e características do sinal:
   - Frequência (`f`) em Hz
   - Taxa de amostragem (`fs`) em Hz
   - Período em amostras (`P = fs/f`)
   - Número total de amostras (`N = dur·fs`)
   - Teorema de Nyquist (`fs > 2f`)

## Conteúdo

### Notebooks (`labs/`)

Todos os notebooks de laboratório da disciplina, organizados por tópico:

- **`labs/le02/`** - Sinais analógicos x digitais e Teorema da Amostragem
  - `le02_pt01_analog-digital-signals.ipynb`
  - `le02_pt02_sampling-theorem.ipynb`
- **`labs/le03_discrete-time-signals/`** - Sinais de tempo discreto
  - `le03_basic-signals.ipynb`
  - `le03_basic-signal-library.ipynb`
- **`labs/le04_karplus-strong/`** - Reconstrução de sinais e síntese Karplus-Strong
  - `le04_01_signal-reconstruction_resolvido.ipynb`:
    - Função `create_sine_signal()` - gera senoides puras
    - Função `SIGNALtone()` - wrapper com fs padrão
    - Função `SIGNALwaveform()` - gera tons com forma de onda aleatória
    - Análise com FFT e visualização espectral
    - Desafios e perguntas respondidas em código

### Módulos Python

- **`signal_functions.py`** - Biblioteca auxiliar com:
  - `create_sine_signal(f, dur, fs)` - cria senoide pura
  - `create_random_sine_signal(dur)` - cria senoide com parâmetros aleatórios

## Conceitos-Chave

### Domínio do Tempo vs. Frequência

Um sinal pode ser visualizado de duas formas:

```
x[n] = A·sin(ω₀·n + φ)   ←→   FFT   ←→   X[k] (espectro)
```

- **Domínio do tempo**: mostra como a amplitude muda a cada amostra
- **Domínio da frequência**: mostra quais frequências estão presentes (via FFT)

### Relação entre Parâmetros

| Símbolo | Significado | Unidade | Relação |
|---------|---|---|---|
| `f` | Frequência (altura da nota) | Hz | `f = fs/P` |
| `fs` | Taxa de amostragem | Hz | `Ts = 1/fs` |
| `P` | Período em amostras | amostras | `P = fs/f` |
| `N` | Total de amostras | amostras | `N = dur·fs` |
| `dur` | Duração | segundos | `dur = N/fs` |

### Teorema de Nyquist

Para amostrar corretamente uma frequência `f`, a taxa de amostragem deve ser:

```
fs > 2f    (ou fs ≥ 2f, dependendo da definição)
```

Se `fs < 2f`, ocorre **aliasing** e você ouve uma frequência errada.

## Como Usar

### Executar um Notebook

```bash
jupyter notebook labs/le04_karplus-strong/le04_01_signal-reconstruction_resolvido.ipynb
```

### Usar as Funções em Python

```python
from signal_functions import create_sine_signal, create_random_sine_signal
import numpy as np

# Criar um tom de 440 Hz (Lá de referência) com 2 segundos
x, fs = create_sine_signal(f=440.0, dur=2.0, fs=44100)

# Criar um sinal aleatório
x, t, fs, f = create_random_sine_signal(dur=1.5)
print(f"Frequência: {f:.2f} Hz, Taxa de amostragem: {fs} Hz")
```

## Resultados Esperados

Ao completar a atividade, você deve entender:

- ✅ Como a FFT decompõe um sinal em suas componentes de frequência
- ✅ Por que a magnitude (`|X[k]|`) é mais informativa que X puro
- ✅ A diferença entre sinal puro (senoide simples) e timbre (forma de onda)
- ✅ Como o Karplus-Strong usa ruído periódico para sintetizar notas musicais realistas

## Referências

- **Transformada Rápida de Fourier (FFT)**: `np.fft.fft()` converte do tempo para frequência
- **Amostragem de Sinais**: Nyquist, Dirac comb, reconstrução interpolada
- **Síntese Karplus-Strong**: base para síntese realista de instrumentos de corda

## Autor

**Caio Moreira Bovo da Cunha Gomes** (202505969)
**Felipe Rodrigues de Sousa** (202504000)

---

**Última atualização**: 02 de outubro de 2026
