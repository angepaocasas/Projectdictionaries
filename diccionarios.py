
def datos_usuarios():

    add_datos = "y"
    lista = []
    while add_datos == "y":
        dictionary = {}
        nombre = str(input("Escribe el nombre a registrar: "))
        edad = int(input("Escribe la edad a registrar: "))
        dictionary.update({nombre: edad})
        lista.append(dictionary)
        add_datos = str(input("Deseas ingresar datos (Y/N):")).lower()
    return lista


resultado = datos_usuarios()


def edad_promedio():
    suma = 0
    for edad in resultado:
        suma_edad = sum(edad.values())
        suma += suma_edad
    return suma / len(resultado)


final = edad_promedio()
print(final)
