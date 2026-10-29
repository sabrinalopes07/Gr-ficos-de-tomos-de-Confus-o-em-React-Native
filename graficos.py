import matplotlib.pyplot as plt
import numpy as np

categorias = [
    'Lack of Indentation no Braces',
    'Assigment as Value',
    'Ommited Curly Braces',
    'Automatic Semicolon Insertion',
    'Object Destructuring',
    
]

valores = [3194, 4667, 17612, 23773, 31684]

y = np.arange(len(categorias))

plt.figure(figsize=(10, 5))
barras = plt.barh(y, valores, height=0.5, color='#83D16B', label='Número de átomos')

plt.bar_label(barras, padding=5)

plt.yticks(y, categorias)
plt.xscale('symlog', linthresh=1000, base=2)
plt.xlim(0, 65536)

# Exibir os valores em vez de potências
plt.xticks(
    [0, 1000, 2000, 4000, 8000, 16000, 32000, 64000],
    ['0', '1.000', '2.000', '4.000', '8.000', '16.000', '32.000', '64.000']
)

plt.title('Top 5 Átomos - React Native')
plt.xlabel('Ocorrências')
plt.legend()
plt.tight_layout()
plt.show()