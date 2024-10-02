import matplotlib.pyplot as plt
import csv


def calcular_media(data):
    return sum(data) / len(data)


def calcular_varianza(data, media):
    return sum((x - media) ** 2 for x in data) / len(data)


def calcular_desviacion_estandar(varianza):
    return varianza**.5


def cargar_datos_csv(nombre_archivo, columna_objetivo):
    fechas = []
    datos_columna = []

    with open(nombre_archivo, newline='') as archivo_csv:
        lector = csv.reader(archivo_csv)
        encabezados = next(lector)

        indice_columna = encabezados.index(columna_objetivo)

        for fila in lector:
            fechas.append(fila[0])
            datos_columna.append(int(fila[indice_columna]))

    return fechas, datos_columna


def graficar_datos(fechas, datos_columna, titulo):
    plt.plot(fechas, datos_columna, color='b', label=titulo, linewidth=2)  
    plt.title(titulo)
    plt.xlabel('Fecha')
    plt.ylabel('Casos')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def seleccionar_estado(encabezados):
    print("\nSelecciona el estado que deseas graficar:")
    for i, estado in enumerate(encabezados[1:-1], 1):
        print(f"{i}. {estado}")

    opcion = int(input("Introduce el número del estado: "))
    return encabezados[opcion]


def menu_principal(encabezados):
    while True:
        print("\nMenú Principal:")
        print("1. Ver datos a nivel Nacional")
        print("2. Ver datos por Estado")
        print("3. Terminar")

        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            return 'Nacional'
        elif opcion == 2:
            return seleccionar_estado(encabezados)
        elif opcion == 3:
            break
        else:
            print("Opción no válida.")
            return menu_principal(encabezados)


def main():
    nombre_archivo = 'covid.csv'

    with open(nombre_archivo, newline='') as archivo_csv:
        lector = csv.reader(archivo_csv)
        encabezados = next(lector)

    columna_objetivo = menu_principal(encabezados)

    if columna_objetivo:
        fechas, datos_columna = cargar_datos_csv(nombre_archivo, columna_objetivo)

        
        media = calcular_media(datos_columna)
        varianza = calcular_varianza(datos_columna, media)
        desviacion_estandar = calcular_desviacion_estandar(varianza)
        maximo = max(datos_columna)
        minimo = min(datos_columna)
        total_casos = sum(datos_columna)

        
        print(f"\nEstadísticas para {columna_objetivo}:")
        print(f"Total de casos: {total_casos}")
        print(f"Media: {media}")
        print(f"Varianza: {varianza}")
        print(f"Desviación Estándar: {desviacion_estandar}")
        print(f"Máximo: {maximo}")
        print(f"Mínimo: {minimo}")

        graficar_datos(fechas, datos_columna, f"Casos Totales - {columna_objetivo}")


if __name__ == "__main__":
    main()
