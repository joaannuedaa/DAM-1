print("Programa lector agenda v0.1 Joan Nueda Gimeno")
archivo = open("agenda.txt",'r')
lineas = archivo.readlines()
for linea in lineas:
    print(linea)
archivo.close()