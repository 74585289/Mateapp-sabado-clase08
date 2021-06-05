import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel()
print(df.head(libro1.xlsx))

variables = df[["estado", "riesgo"]]

colores = ["red", "red", "red", "green", "green", "green"]

desarrollo_grafico = variables.plot.barh(x="estado", y = "riesgo", color = colores)
plt.xlabel("Cantidad por %")
plt.ylabel("cituacion")
plt.title("cituacion de contagios en todo el peru")
plt.savefig("contagios_covid")
plt.show