import pickle

frutas = []

archivo = open('frutas.bin', 'rb')
frutas = pickle.load(archivo)
print(frutas)
archivo.close()