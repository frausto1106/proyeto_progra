import matplotlib.pyplot as plt
import csv



def cargarDatos(col):
    fechas = []
    datos = []

    with open("covid.csv", newline='') as archivo_csv:
        lector = csv.reader(archivo_csv)
        encabezados = next(lector)

        i = encabezados.index(col)

        for fila in lector:
            fechas.append(fila[0])
            datos.append(int(fila[i]))

    return fechas, datos

def grafica(fechas, datos_columna, titulo):
    plt.plot(fechas, datos_columna, color='b', label=titulo, linewidth=2)
    plt.title(titulo)
    plt.xlabel('Fecha')
    plt.ylabel('Casos')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()



def nacionales():
    with open("covid.csv", newline='') as archivo_csv:
        lector = csv.reader(archivo_csv)
        encabezados = next(lector)

    print("\nEstadísticas por Estado:")

    for estado in encabezados[1:-1]:
        fechas, datos = cargarDatos(estado)

        media = sum(datos) / len(datos)
        difs = [(x - media) ** 2 for x in datos]
        varianza = sum(difs) / len(datos)
        desviacionEstandar = varianza ** 0.5
        maximo = max(datos)
        minimo = min(datos)
        tot = sum(datos)

        print(f"\nEstadísticas para {estado}:")
        print(f"Total de casos: {tot}")
        print(f"Media: {media}")
        print(f"Varianza: {varianza}")
        print(f"Desviación Estándar: {desviacionEstandar}")
        print(f"Máximo: {maximo}")
        print(f"Mínimo: {minimo}")

    col = 'Nacional'
    fechas, datos = cargarDatos(col)

    media = sum(datos) / len(datos)
    difs = [(x - media) ** 2 for x in datos]
    varianza = sum(difs) / len(datos)
    desviacionEstandar = varianza ** 0.5
    maximo = max(datos)
    minimo = min(datos)
    tot = sum(datos)

    print(f"\nEstadísticas para {col}:")
    print(f"Total de casos: {tot}")
    print(f"Media: {media}")
    print(f"Varianza: {varianza}")
    print(f"Desviación Estándar: {desviacionEstandar}")
    print(f"Máximo: {maximo}")
    print(f"Mínimo: {minimo}")



def estado():
    with open("covid.csv", newline='') as archivo_csv:
        lector = csv.reader(archivo_csv)
        encabezados = next(lector)

    print("\nSelecciona el estado que deseas: ")
    for i, estado in enumerate(encabezados[1:-1], 1):
        print(f"{i}. {estado}")

    opc = int(input("Introduce el número del estado: "))


    state = encabezados[opc]

    fechas, datos = cargarDatos(state)

    media = sum(datos) / len(datos)
    difs = []

    for x in datos:
        dif = x - media
        difs.append(dif ** 2)

    varianza = sum(difs) / len(datos)
    desviacionEstandar = varianza ** 0.5
    maximo = max(datos)
    minimo = min(datos)
    tot = sum(datos)

    print(f"\nEstadísticas para {state}")
    print(f"Total de casos: {tot}")
    print(f"Media: {media}")
    print(f"Varianza: {varianza}")
    print(f"Desviación Estándar: {desviacionEstandar}")
    print(f"Máximo: {maximo}")
    print(f"Mínimo: {minimo}")

    fileName = f"{state}.txt"

    with open(fileName, 'w') as archivo:
        archivo.write(f' {state}  \n')
        archivo.write(f' Total de casos: {tot}  \n')
        archivo.write(f' Media: {media}  \n')
        archivo.write(f' Varianza: {varianza}  \n')
        archivo.write(f' Desviación Estándar: {desviacionEstandar}  \n')
        archivo.write(f' Máximo: {maximo}  \n')
        archivo.write(f' Mínimo: {minimo}  \n')

    grafica(fechas, datos, f"Casos Totales - {state}")

while True:
    print("\nMenú Principal:")
    print("1. Ver datos a nivel Nacional")
    print("2. Ver datos por Estado")
    print("3. Terminar")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        nacionales()
    elif opcion == 2:
        estado()
    elif opcion == 3:
        break
    else:
        print("Opción no válida.")