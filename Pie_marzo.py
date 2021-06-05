import matplotlib.pyplot as plt
labels = 'Productos', 'Gastos','Ganancias' , 'Distribucion', 'Impuestos'
sizes = [1500,4500 ,5000, 3375, 900]
explode = (0, 0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()

ax1.pie(sizes, explode=explode, labels=labels, autopct='%0.1f%%',
        shadow=True, startangle=90   )

ax1.axis('equal')  

plt.title("Ventas del mes de marzo")
plt.show()