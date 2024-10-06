import matplotlib.pyplot as plt
import csv



def cargar_datos_csv(col):
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





def mostrar_datos_nacionales():
    col = 'Nacional'
    fechas, datos = cargar_datos_csv('covid.csv', col)

    media = sum(datos) / len(datos)
    difs = []

    for x in datos:
        dif = x - media
        difs.append(dif ** 2)

    varianza = sum(difs) / len(datos)
    desviacionEstandar = varianza ** 0.5
    maximo = max(datos)
    minimo = min(datos)
    total_casos = sum(datos)

    print(f"\nEstadísticas para {col}:")
    print(f"Total de casos: {total_casos}")
    print(f"Media: {media}")
    print(f"Varianza: {varianza}")
    print(f"Desviación Estándar: {desviacionEstandar}")
    print(f"Máximo: {maximo}")
    print(f"Mínimo: {minimo}")

    graficar_datos(fechas, datos, f"Casos Totales - {col}")




def mostrar_datos_por_estado():
    with open("covid.csv", newline='') as archivo_csv:
        lector = csv.reader(archivo_csv)
        encabezados = next(lector)

    print("\nSelecciona el estado que deseas graficar:")
    for i, estado in enumerate(encabezados[1:-1], 1):
        print(f"{i}. {estado}")

    opc = int(input("Introduce el número del estado: "))


    col = encabezados[opc]

    fechas, datos = cargar_datos_csv(col)

    media = sum(datos) / len(datos)
    difs = []

    for x in datos:
        dif = x - media
        difs.append(dif ** 2)

    varianza = sum(difs) / len(datos)
    desviacionEstandar = varianza ** 0.5
    maximo = max(datos)
    minimo = min(datos)
    total_casos = sum(datos)

    print(f"\nEstadísticas para {col}:")
    print(f"Total de casos: {total_casos}")
    print(f"Media: {media}")
    print(f"Varianza: {varianza}")
    print(f"Desviación Estándar: {desviacionEstandar}")
    print(f"Máximo: {maximo}")
    print(f"Mínimo: {minimo}")

    graficar_datos(fechas, datos, f"Casos Totales - {col}")

def menu_principal():
    while True:
        print("\nMenú Principal:")
        print("1. Ver datos a nivel Nacional")
        print("2. Ver datos por Estado")
        print("3. Terminar")

        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            mostrar_datos_nacionales()
        elif opcion == 2:
            mostrar_datos_por_estado()
        elif opcion == 3:
            break
        else:
            print("Opción no válida.")

def main():
    menu_principal()

if __name__ == "__main__":
    main()
