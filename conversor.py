def conversor(tipo_pesos, valor_dolar):
    pesos = input('Cuantos pesos' + tipo_pesos + ' tienes?: ')
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

menu = """
Bienvenido al conversor de monedas ✨ 

1. Pesos Colombianos
2. Pesos argentinos
3. Pesos Mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor('Colombianos', 3875)
elif opcion == 2:
    conversor('Argentinos', 65)   
elif opcion == 3:
    conversor('Mexicanos', 24)    
else:
    print('Ingresa un opcion correcta')




# menu = """
# Bienvenido al conversor de monedas ✨ 

# 1. Pesos Colombianos
# 2. Pesos argentinos
# 3. Pesos Mexicanos

# Elige una opcion: """

# opcion = int(input(menu))

# if opcion == 1:
#     pesos = input('Cuantos pesos Colombianos tienes?: ')
#     pesos = float(pesos)
#     valor_dolar = 3875
#     dolares = pesos / valor_dolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("Tienes $" + dolares + " dolares")
# elif opcion == 2:
#     pesos = input('Cuantos pesos Argentinos tienes?: ')
#     pesos = float(pesos)
#     valor_dolar = 65
#     dolares = pesos / valor_dolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("Tienes $" + dolares + " dolares")
# elif opcion == 3:
#     pesos = input('Cuantos pesos Mexicanos tienes?: ')
#     pesos = float(pesos)
#     valor_dolar = 24
#     dolares = pesos / valor_dolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("Tienes $" + dolares + " dolares")
# else:
#     print('Ingresa un opcion correcta')


