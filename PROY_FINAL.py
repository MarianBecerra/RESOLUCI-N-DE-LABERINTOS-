import os

class SolucionadorLab:
    def __init__(self):
        self.grafo = {}

    def agregar_interseccion(self, interseccion, conexiones):
        self.grafo[interseccion] = conexiones

    def resolver_laberinto(self, inicio, fin):
        visitados = set()
        cola = [[inicio]]

        if inicio not in self.grafo or fin not in self.grafo:
            return None  # No se puede resolver si el inicio o el fin no estan en el grafo

        while cola:
            camino = cola.pop(0)
            nodo_actual = camino[-1]

            if nodo_actual == fin:
                return camino

            if nodo_actual not in visitados:
                vecinos = self.grafo[nodo_actual]
                for vecino in vecinos:
                    nuevo_camino = list(camino)
                    nuevo_camino.append(vecino)
                    cola.append(nuevo_camino)

                visitados.add(nodo_actual)

        return None  # No se encontro un camino

    # Funcion para mostrar el laberinto
    def mostrar_laberinto(self):
        nodos = list(self.grafo.keys())  # Obtener todos los nodos del grafo
        nodos.sort()  # Ordenar los nodos alfabéticamente para imprimir la matriz de manera ordenada

        # Imprimir la primera fila con los nombres de los nodos
        print("    " + "   ".join(nodos))

        # Imprimir la matriz de adyacencia
        for nodo in nodos:
            fila = [str(int(nodo_destino in self.grafo[nodo])) for nodo_destino in nodos]
            print(f"{nodo} | {'   '.join(fila)}")


laberinto = SolucionadorLab()

while True:
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

    print("\nSolucionador de laberintos\n")
    print(" ------------------------------------------- \n")
    print("1. Ingresar laberinto\n")
    print("2. Solucionar laberinto\n")
    print("3. Mostrar laberinto\n")
    print("4. Salir\n")

    eleccion = input("\nDigite su eleccion: ")

    if int(eleccion) == 1: # Ingresar laberinto
        while True:
            interseccion = input("\nIngrese la interseccion (o 'fin' para terminar): ")
            if interseccion.lower() == 'fin':
                break

            conexiones = input("Ingrese los nodos vecinos (separadas por coma): ").split(',')
            laberinto.agregar_interseccion(interseccion, conexiones)

        input("\nLaberinto ingresado. Presione Enter para continuar... ")
    elif int(eleccion) == 2: # Solucionar laberinto
        inicio = input("\nIngrese el punto de inicio: ")
        fin = input("Ingrese el punto de destino: ")
        camino_resuelto = laberinto.resolver_laberinto(inicio, fin)
        if camino_resuelto:
            print("Camino resuelto: " + str(camino_resuelto))
        else:
            print("No hay camino posible.")
        input("\nPresione Enter para continuar... ")
    elif int(eleccion) == 3: # Mostrar laberinto
        laberinto.mostrar_laberinto()
        input("\nPresione Enter para continuar... ")
    elif int(eleccion) == 4:
        print("\nSaliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("\nOpcion no valida. Por favor, elija una opcion valida.")
        input("\nPresione Enter para continuar... ")
