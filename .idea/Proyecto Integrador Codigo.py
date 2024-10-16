import matplotlib.pyplot as plt
import csv

def cargar_datos(columna):
    fechas = []
    datos = []

    with open("covid.csv", newline='') as archivo_csv:
        lector = csv.reader(archivo_csv)
        encabezados = next(lector)

        indice_columna = encabezados.index(columna)

        for fila in lector:
            fechas.append(fila[0])
            datos.append(int(fila[indice_columna]))

    return fechas, datos

def graficar_datos(fechas, datos, titulo):
    plt.plot(fechas, datos, color='b', label=titulo, linewidth=2)
    plt.title(titulo)
    plt.xlabel('Fecha')
    plt.ylabel('Casos')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def calcular_estadisticas(datos):
    media = sum(datos) / len(datos)
    varianza = sum((x - media) ** 2 for x in datos) / len(datos)
    desviacion_estandar = varianza ** 0.5
    total_casos = sum(datos)
    maximo = max(datos)
    minimo = min(datos)

    return total_casos, media, varianza, desviacion_estandar, maximo, minimo

def guardar_estadisticas(estado, total_casos, media, varianza, desviacion_estandar, maximo, minimo):
    with open(f"{estado}_estadisticas.txt", "w") as archivo:
        archivo.write(f"Estadísticas para {estado}:\n")
        archivo.write(f"Total de casos: {total_casos}\n")
        archivo.write(f"Media: {media}\n")
        archivo.write(f"Varianza: {varianza}\n")
        archivo.write(f"Desviación Estándar: {desviacion_estandar}\n")
        archivo.write(f"Máximo: {maximo}\n")
        archivo.write(f"Mínimo: {minimo}\n")

def estadisticas_nacionales():
    with open("covid.csv", newline='') as archivo_csv:
        lector = csv.reader(archivo_csv)
        encabezados = next(lector)

        print(f"\nEstadísticas nacionales:")
        fechas_nacionales, datos_nacionales = cargar_datos('Nacional')

        estadisticas_nacionales = calcular_estadisticas(datos_nacionales)
        print(f"Total de casos: {estadisticas_nacionales[0]}")
        print(f"Media: {estadisticas_nacionales[1]}")
        print(f"Varianza: {estadisticas_nacionales[2]}")
        print(f"Desviación Estándar: {estadisticas_nacionales[3]}")
        print(f"Máximo: {estadisticas_nacionales[4]}")
        print(f"Mínimo: {estadisticas_nacionales[5]}")

        for estado in encabezados[1:]:
            fechas_estado, datos_estado = cargar_datos(estado)
            estadisticas_estado = calcular_estadisticas(datos_estado)

            print(f"\nEstadísticas para {estado}:")
            print(f"Total de casos: {estadisticas_estado[0]}")
            print(f"Media: {estadisticas_estado[1]}")
            print(f"Varianza: {estadisticas_estado[2]}")
            print(f"Desviación Estándar: {estadisticas_estado[3]}")
            print(f"Máximo: {estadisticas_estado[4]}")
            print(f"Mínimo: {estadisticas_estado[5]}")

def datos_estado():
    with open("covid.csv", newline='') as archivo_csv:
        lector = csv.reader(archivo_csv)
        encabezados = next(lector)

    print("\nSelecciona el estado que deseas graficar:")
    for i, estado in enumerate(encabezados[1:], 1):
        print(f"{i}. {estado}")

    opcion = int(input("Introduce el número del estado: ")) - 1
    columna = encabezados[opcion + 1]

    fechas, datos = cargar_datos(columna)

    estadisticas_estado = calcular_estadisticas(datos)

    print(f"\nEstadísticas para {columna}:")
    print(f"Total de casos: {estadisticas_estado[0]}")
    print(f"Media: {estadisticas_estado[1]}")
    print(f"Varianza: {estadisticas_estado[2]}")
    print(f"Desviación Estándar: {estadisticas_estado[3]}")
    print(f"Máximo: {estadisticas_estado[4]}")
    print(f"Mínimo: {estadisticas_estado[5]}")

    guardar_estadisticas(columna, *estadisticas_estado)
    print(f"Las estadísticas se han guardado en '{columna}_estadisticas.txt'.")

    graficar_datos(fechas, datos, f"Casos Totales - {columna}")

def menu_principal():
    while True:
        print("Menú Principal:")
        print("1. Ver estadísticas generales.")
        print("2. Ver datos por estado.")
        print("3. Terminar programa.")

        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            estadisticas_nacionales()
        elif opcion == 2:
            datos_estado()
        elif opcion == 3:
            break
        else:
            print("Opción no válida.")

def main():
    menu_principal()

main()
