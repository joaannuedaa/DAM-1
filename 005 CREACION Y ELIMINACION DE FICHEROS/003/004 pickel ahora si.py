import pickle

frutas = ['manzana','pera','platano']

archivo = open('frutas.bin', 'wb')
pickle.dump(frutas, archivo)