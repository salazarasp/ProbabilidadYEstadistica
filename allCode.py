# Con la importación traemos las librerías que necesitamos a nuestro código.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import matplotlib.backends.backend_pdf
# Importamos los datos.
data=pd.read_csv(r"monthly_salary_brazil.csv")
# De la tabla que importamos desde el csv, obtenemos solo la columna del salario total.
salaries=data["total_salary"]
# Algunos valores de datos son inferiores a cero.
# Eso no tiene sentido ya que los salarios deben ser mayores que cero.
# Así que hacemos un corte de los datos.
real_salaries=salaries[salaries>0]
# Desde una gráfica de caja podemos visualizar que los datos están más concentrados antes de 5000.
# Por lo tanto, hacemos un corte en los datos para ver el comportamiento en esa región
soi=real_salaries[real_salaries<5000]
# Calculamos el número de clases para el histograma con la fórmula log (n) / log (2).
# Hacemos uso de la biblioteca de matemáticas (math).
number_of_classes=int(round(math.log(soi.size)/math.log(2)))
# Realizamos una gráfica del histograma.
# La función hist, devuelve tres matrices, que contienen las frecuencias de las clases,
# los contenedores de las clases y otra matriz que no es de nuestro interés.
# La matriz de bins contiene los límites de las clases.
freq,bins,patches=plt.hist(soi,bins=number_of_classes,edgecolor="black")
# Esta función simplemente limpia la trama.
# En realidad, la línea anterior era solo para obtener la frecuencia y los intervalos para nuestra tabla de frecuencias,
# por lo que podemos limpiar cualquier función que se haya trazado.
plt.cla()
# Podemos calcular las frecuencias relativas utilizando la fórmula:
# frecuencia relativa = frecuencia / número de datos
rel_freq=freq/soi.size
# Vamos a crear una serie de rango de clases.
# En primer lugar, lo dejamos vacío para que podamos agregar nuevos valores.
class_range=[]
# Crearemos una serie de clases superiores.
# En primer lugar, lo dejamos vacío para que podamos agregar nuevos valores.
upper_class=[]
# Vamos a crear una serie de clases medias.
# En primer lugar, lo dejamos vacío para que podamos agregar nuevos valores.
# Esta matriz contendrá la marca de clases que es solo el promedio de la clase superior e inferior.
middle_class=[]
# Recorremos todos los elementos de la matriz de bins que contiene los límites de las clases.
# Agregamos los valores correspondientes a las matrices.
for i in range(int(bins.size)-1):
    lower=bins[1]
    upper=bins[i+1]
    upper_class.append(upper)
    middle_class.append((upper+lower)/2)
# En el aviso de rango de clase que estamos agregando una cadena
# Esa cadena será "inferior-superior", con el signo "+", solo le decimos a Python que se una a las cadenas.
# La función de agregar inserta un nuevo valor al final de la matriz.
# Entonces, como puede observar, comenzamos con una matriz vacía y luego agregamos un valor cada vez.
# Entonces, podemos pensar así con el siguiente ejemplo:
# Entra en el bucle class_range = [] (vacío), luego agrega class_range = [0-10]
# ingresa una vez más en el loop y agrega una vez más class_range = [0-10,10-20] y así sucesivamente.
    class_range.append("{:0.2f}".format(lower)+"-"+"{:0.2f}".format(upper))

#   Histograma de frecuencia acumulativa.

# La función hist devuelve tres matrices.
# Las matrices trash1 y trash2 son solo matrices que no utilizaremos.
# Sin embargo, ya que estamos interesados ​​en las frecuencias acumulativas, debemos recibir las tres matrices si queremos a ""cum freq"".
cumfreq,trash1,trash2=plt.hist(soi,bins=number_of_classes,edgecolor="black",cumulative=True)
# Creamos una tabla de datos con columnas "Frecuencia", "Frecuencia relativa", "Marca de clase" ...
# Estas columnas contendrán los vectores correspondientes freq, real freq, ...
Table=pd.DataFrame({"Frequency":freq,"Relative Frequency":rel_freq,"Mark of Class":middle_class, "Cumulative Frequency":cumfreq},index=class_range)
# Hacemos que la pantalla de salida solo tenga 2 decimales.
pd.set_option('precision',2)
# Imprimimos la tabla (el marco de datos).
print(Table)

#   Ojive

# Note que usamos plot y no hist o cualquier otro método de ploteado usado antes.
# La función de trazado en realidad traza los puntos (x, y) de dos matrices en los ejes "y" y "x".
# Entonces, en este caso, en los valores del eje x serán los valores de upper_class y en los valores del eje y será el cumfreq.
# Así que tenemos tuplas (upper_class, cumfreq).
# El 'go-' está indicando a la función de trazado que cree el trazado con "líneas verdes" y que une los valores de los puntos con o.
# Así que si escribes 'rx-', la línea sería roja, conectada con cruces
plt.plot(upper_class,cumfreq,'go-')
# Guardamos todas las figuras en un pdf.
# Creamos el archivo con el nombre "output.pdf"
pdf=matplotlib.backends.backend_pdf.PdfPages("output.pdf")
# Convertir tabla a archivo de Excel.
# Hacemos que el marco de datos se guarde también como archivo de excel
Table.to_excel("FrecuenciesTable.xlsx",float_format="%.2f")
# Agregar figura
# Creamos una figura en pulgadas.
# El primer número en la figura es el ancho y el segundo es la altura de la figura.
# Una figura es el cuadro completo donde puede agregar tantas gráficas como desee,
# así que usaremos la función add_subplot para agregar una nueva gráfica
figure=plt.figure(figsize=(8,30))
# Número de gráficas.
n=7

#   Histograma de frecuencia

# Cada figura tiene divisiones.
#Añadimos nuestra primera subdivision.
# Observe que la n indica el número de filas,
# el número 1 en la segunda ranura es el número de columnas.
# Finalmente, el tercer número con 1, indica el índice de la división que estamos creando.
ax=figure.add_subplot(n,1,1)
freq,bins,patches=ax.hist(soi,bins=number_of_classes,edgecolor="black",color="green")

#   Histograma de frecuencia acumulativa

ax=figure.add_subplot(n,1,2)
cum_freq,trash,trash=ax.hist(soi,bins=number_of_classes,edgecolor="black",cumulative=True)


#   Histograma de frecuencia relativa acumulativa

# Con las siguientes dos líneas de código creamos una matriz con números [1/n,1/n,...,1/n].
# En primer lugar, con la función "np.zeros(soi.size)"
# le estamos diciendo a python que cree una matriz de "size soi.size" llena de ceros.
# Luego, con "zeros_vector+1/soi.size" en cada ranura, sumamos "1/n",
# donde "n" es el número de datos, obtenidos con "soi.size"
zeros_vector=np.zeros(soi.size)
w_array=zeros_vector+1/soi.size
ax=figure.add_subplot(n,1,3)

# Cuando llamamos a ponderaciones = w_array le estamos diciendo a la función "Para cada uno de los datos, den cierto peso de conteo".
# Por ejemplo, para la matriz de datos [1,2,3,4]...la matriz de ponderaciones con ponderaciones
# [3,7,9,10] diría a la función contar el número "1"-> como 3 veces, el valor "2" lo cuenta como 7 veces
# y así sucesivamente y así sucesivamente.
# Observa que pasamos una matriz con números [1/n,1/n,1/n,1/n,1/n,1/n,1/n,1/n,....] donde n es el numero de datos.
# Entonces estamos contando cada valor "1/n".
# Esa es la definición de la frecuencia relativa.
cum_rel_freq,trash1,trash2=ax.hist(soi,bins=number_of_classes,edgecolor="black",cumulative=True,weights=w_array,color="orange")
plt.title("Most Common Brazilian People Salaries")
plt.xlabel("Salaries")
plt.ylabel("Number of People")

#   Frecuencias acumulativas de Ogive.
ax=figure.add_subplot(n,1,4)
plt.title("Ogive Most Common Brazilian People Salaries")
ax.plot(upper_class,cum_freq,'ro-')

#   Boxplot.

# Diagrama de caja (observe que este cuadro de caja es de TODOS los datos,
# no solo los datos recortados 0 <salarios <5000).
ax=figure.add_subplot(n,1,5)
ax.boxplot(salaries,vert=False)

#   Ogive Frecuencias Relativas Acumulativas.

ax=figure.add_subplot(n,1,6)
ax.plot(upper_class,cum_rel_freq,'go-')

#   Polígono de frecuencias.

R_class=bins[1]-bins[0]
mcfp=middle_class
print(middle_class[-1])
print(R_class)
mcfp.insert(int(len(middle_class)),middle_class[-1]+R_class)
mcfp.insert(0,middle_class[0]-R_class)

# Frecuencias para polígono.

ffp=freq.tolist()
ffp.append(0)
ffp.insert(0,0)
ax=figure.add_subplot(n,1,7)
ax.plot(mcfp,ffp,"-ro")

# Guardando la primera figura en un pdf-
pdf.savefig(figure)


# Guardando la primera figura en un archivo png plt.savefig ("test1.png").
# Creando la segunda figura para algunos otros gráficos
# (Los gráficos circulares).

figure2=plt.figure(figsize=(20,20))

# Esta línea de código creará una tabla con los valores del sector de columna de la tabla de datos.
# Esa columna, como se puede observar, si abre el archivo de Excel contiene todos los "nombres de trabajos".
# Así obtendrá una tabla con los trabajos y la cantidad de veces que el trabajo se repite en la columna o la frecuencia del trabajo.
# Podemos lograr esto con la función hermosa y sorprendente .value_counts ().
# Verificará los valores repetidos en cierta columna, los contará y le devolverá la tabla.

# Así por ejemplo. Imagina que tienes los siguientes datos en el sector columna:

# Ingeniero
# Abogado
# Profesor
# Artista
# Ingeniero
# Abogado
# Ingeniero
# Policía
# Ingeniero

# con sector_counts volvería
# Ingeniero 4
# Abogado 2
# Profesor 1
# Artista 1
# Policía 1

sector_counts= data["sector"].value_counts()
print(sector_counts)

# Dividir los datos en tres conjuntos diferentes, para que podamos visualizar los datos en los gráficos circulares.
# La primera división
alljobs_final=sector_counts[sector_counts>=2000]
# El segundo conjunto, solo aquellos valores por debajo de 2000 y mayores de 150 (el segundo corte en las siguientes líneas).
# El resto está contenido como "Very Unlikely Jobs".
less_common_sect=sector_counts[sector_counts<2000]
# Very unlikely jobs. Solo aquellos por debajo de 150.
very_unlikely_jobs=less_common_sect[less_common_sect<150]
# Segundo corte aplicado a less_common_sect.
less_common_sect=less_common_sect[less_common_sect>150]
# Necesitamos incluir los trabajos menos comunes a todos los trabajos
# por lo que hay que crear otro objeto pandas.
other=pd.Series([less_common_sect.sum()],index=["Less Common Jobs"])
alljobs_final=alljobs_final.append(other)
# Necesitamos incluir los valores muy poco probables en el campo común,
# entonces creamos otro objeto pandas
vul=pd.Series([very_unlikely_jobs.sum()],index=["Very Unlikely Jobs"])
# Añadimos los valores muy poco probables.
less_common_sect=less_common_sect.append(vul)
# Creamos matrices de etiquetas. Los labels serán los nombres de los trabajos.
# Se almacenan en nuestros índices de los arrays.
# También agregamos a las etiquetas el porcentaje de cada trabajo.
alabels_final=[alljobs_final.index[i] +" "+"{:0.3f}".format(alljobs_final[i]/data["sector"].size*100) + "%" for i in range (alljobs_final.size)]

alabels_lscommon=[less_common_sect.index[i] +" "+ "{:0.3f}".format(less_common_sect[i]/data["sector"].size*100) + "%" for i in range (less_common_sect.size)]

alabels_vul=[very_unlikely_jobs.index[i] +" "+ "{:0.4f}".format(very_unlikely_jobs[i]/data["sector"].size*100)+ "%" for i in range (very_unlikely_jobs.size)]

# Esto creará el mapa de colores.
# Visite https://matplotlib.org/examples/color/colormaps_reference.html,
# para ver la nomenclatura de diferentes colores.
cmap=plt.get_cmap('RdYlBu')
acolors=[cmap(i) for i in np.linspace(0,1,8)]


# Esto creará una matriz que le dirá a la grafica cómo compensar las etiquetas y las porciones de la misma.
explode_1=np.zeros(alljobs_final.size)
for i in range (1,10):
    explode_1[-i]=2.5-i*0.13

explode_2=np.zeros(less_common_sect.size)
for i in range (1,22):
    explode_2[-i]=3-i*0.13
explode_3=np.zeros(very_unlikely_jobs.size)
explode_3[-1]=4
explode_3[-2]=2.8
explode_3[-3]=1.6
explode_3[-4]=0.4
# Añadimos la primer grafica de pastel
ax2=figure2.add_subplot(3,1,1)
ax2.set_title("All Jobs",x=-0.2,fontsize=25)
ax2.pie(alljobs_final,colors=acolors,
        labels=alabels_final,explode=explode_1,rotatelabels=True)
# Añadimos la segunda grafica de pastel
ax2=figure2.add_subplot(3,1,2)
# Dando un título a la trama.
ax2.set_title("Less Common Jobs ",x=1.7,fontsize=25)
ax2.pie(less_common_sect,colors=acolors,labels=alabels_lscommon,explode=explode_2, rotatelabels=True)
# Añadimos la tercer grafica de pastel
ax2=figure2.add_subplot(3,1,3)
ax2.set_title("Very Unlikely Jobs ",x=1.7,fontsize=25)
ax2.pie(very_unlikely_jobs,colors=acolors,
        labels=alabels_vul,explode=explode_3,rotatelabels=True)
print(very_unlikely_jobs)

# Ajustar el espacio entre plots.
plt.subplots_adjust(hspace=0.8)

# Guardamos en el pdf lo que hemos hecho en la segunda figura
# pdf.savefig (figura 2)
pdf.savefig(figure2)
#Cerramos el pdf. Si no escribimos este comando, no podremos abrir nuestro archivo pdf.
pdf.close()