import matplotlib.pyplot as plt
labels = 'Productos', 'Gastos','Ganancias' , 'Distribucion', 'Impuestos'
sizes = [3000,	5500,	3000,	6000,	540]
explode = (0, 0, 0, 0.1, 0)  

fig1, ax1 = plt.subplots()

ax1.pie(sizes, explode=explode, labels=labels, autopct='%0.1f%%',
        shadow=True, startangle=90   )

ax1.axis('equal')  

plt.title("Ventas del mes de mayo")
plt.show()