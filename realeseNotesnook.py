import matplotlib.pyplot as plt

# Categorias e valores
categorias = ["2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026"]
valores = [117, 1281, 537, 3886, 4642, 5648, 6377, 6750]

# Criar o gráfico de barras
plt.bar(categorias, valores, color="skyblue", width=0.5, label="Número de átomos")

# Adicionar títulos e rótulos
plt.title("Gráfico das releases dos 5 maiores projetos - Notesnook")
plt.xlabel("Ano")
plt.ylabel("Número de átomos")

# Exibir os valores nas barras
plt.bar_label(plt.gca().containers[0], padding=3)

# Exibir o gráfico
plt.tight_layout()
plt.show()