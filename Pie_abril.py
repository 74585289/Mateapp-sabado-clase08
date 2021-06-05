import matplotlib.pyplot as plt
labels = 'Productos', 'Gastos','Ganancias' , 'Distribucion', 'Impuestos'
sizes = [2075,4595,5396,4000,972]
explode = (0, 0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()

ax1.pie(sizes, explode=explode, labels=labels, autopct='%0.1f%%',
        shadow=True, startangle=90   )

ax1.axis('equal')  

plt.title("Ventas del mes Abril")
plt.show()