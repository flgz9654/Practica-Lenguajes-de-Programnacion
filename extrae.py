# Codigo para extraer un substring

# Primer metodo para extraer un substring en un string definido

string1 = 'Seremos los mejores en programacion'
substring = string1[8:19]

print(substring, 'en Python')

# Segundo metodo para extraer solicitando una frase por pantalla

frase = input('Ingresa una frase: ')
print('Digita la posicion inicial a extraer: ')
posicion_inicial = int(input())
print('Digita la posicion final a extraer: ')
posicion_final = int(input())

subfrase = frase[posicion_inicial:posicion_final]

print(subfrase)