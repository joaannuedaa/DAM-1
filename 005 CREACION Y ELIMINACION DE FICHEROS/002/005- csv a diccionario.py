archivo = open('clientes.csv','r')
# Solo leemos la primera linea
with open("clientes.csv", "r", encoding="utf-8") as archivo:
    cabecera = archivo.readline()  # Singular
# Partimos la primera linea en una lista de cabeceras de columna
cabeceras = cabecera.split("|")
# Ahora sí ya lo leemos todo
with open("clientes.csv", "r", encoding="utf-8") as archivo:
    cabecera = archivo.readline()
    lineas = archivo.readlines()  # Plural
# Recorro todas las lineas
for linea in lineas:
    # Parto una linea completa en campos individuales
    datos = linea.split("|")
    for i in range(0, len(datos)):
        print(cabeceras[i], ":", datos[i])