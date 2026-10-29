import matplotlib.pyplot as plt

# Categorias e valores
categorias = ["2016","2017","2018","2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026"]
valores = [27, 1932, 2783, 3209, 4682, 5836, 5998, 6447, 6648, 7195, 8726]

# Criar o gráfico de barras
plt.bar(categorias, valores, color="skyblue", width=0.5, label="Número de átomos")

# Adicionar títulos e rótulos
plt.title("Gráfico das releases dos 5 maiores projetos")
plt.xlabel("Ano")
plt.ylabel("Número de átomos")

# Exibir os valores nas barras
plt.bar_label(plt.gca().containers[0], padding=3)

# Exibir o gráfico
plt.tight_layout()
plt.show()