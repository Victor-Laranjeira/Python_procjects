# Visualização de dados em Python

# import matplotlib.pyplot as plt
#
# x = [1, 2, 5]
# y = [2, 3, 7]
#
# # Título
# plt.title("Título do gráfico")
#
# # Eixos
# plt.xlabel("Eixo x")
# plt.ylabel("Exixo y")
#
# plt.plot(x, y)
# plt.show()

#################################################################################################################

# Gráfico em barra

# import matplotlib.pyplot as plt
#
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 7, 1, 0]
#
# titulo = "Gráfico de barras"
# eixox = "Eixo x"
# eixoy = "Eixo y"
#
# # Legendas
# plt.title(titulo)
# plt.xlabel(eixox)
# plt.ylabel(eixoy)
#
# plt.bar(x, y)
# plt.show()

################################################################################################################

# Comparaçãode gráficos em barras

# import matplotlib.pyplot as plt
#
# x1 = [1, 3, 5, 7, 9]
# y1 = [2, 3, 7, 1, 0]
#
# x2 = [2, 4, 6, 8, 10]
# y2 = [5, 1, 3, 7, 4]
#
# titulo = "Gráfico de barras"
# eixox = "Eixo x"
# eixoy = "Eixo y"
#
# # Legendas
# plt.title(titulo)
# plt.xlabel(eixox)
# plt.ylabel(eixoy)
#
# plt.bar(x1, y2, label = "Grupo 1")
# plt.bar(x2, y2, label = "grupo 2")
# plt.legend()
#
# plt.show()

################################################################################################################

# Gráfico de dispersão

# import matplotlib.pyplot as plt
#
# x = [1, 3, 5, 7, 9]
# y = [2, 3, 7, 1, 0]
#
#
# titulo = "Gráfico de dispersão"
# eixox = "Eixo x"
# eixoy = "Eixo y"
#
# # Legendas
# plt.title(titulo)
# plt.xlabel(eixox)
# plt.ylabel(eixoy)
#
# plt.scatter(x, y, label = "Grupo 1", color="Cyan")
# plt.plot(x, y)
# plt.legend()
# # plt.show()
# plt.savefig("figura1.png", dpi=300) # "figura1.pdf"

##############################################################################################################

# Diagrama de caixas

# import matplotlib.pyplot as plt
# import random
#
# vetor = []
#
# for i in range(10):
#     numero_aleatorio = random.randint(0, 10)
#     vetor.append(numero_aleatorio)
#
# plt.boxplot(vetor)
# plt.title("Boxplot")
# plt.show()

###############################################################################################################
