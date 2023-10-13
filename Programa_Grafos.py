import networkx as nx
import matplotlib.pyplot as plt

def lista_a_matriz(lista):
    n = len(lista)
    matriz = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in lista[i]:
            matriz[i][j] = 1
    return matriz

def matriz_a_lista(matriz):
    lista = []
    for i, fila in enumerate(matriz):
        adyacentes = [j for j, valor in enumerate(fila) if valor == 1]
        lista.append(adyacentes)
    return lista

def dibujar_grafo(lista):
    G = nx.Graph()
    for nodo, adyacentes in enumerate(lista):
        G.add_node(nodo)
        for adyacente in adyacentes:
            G.add_edge(nodo, adyacente)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_color='black', font_weight='bold')
    plt.title("Representación gráfica del grafo :)")
    plt.show()

def main():
    print("¿Cómo desea ingresar el grafo?")
    print("1. Lista de adyacencia")
    print("2. Matriz de adyacencia")
    opcion = int(input("Ingrese la opción: "))

    if opcion == 1:
        lista_adyacencia = eval(input("Ingrese la lista de adyacencia (por ejemplo, [[1, 2], [0, 2], [0, 1]]): "))
        matriz_adyacencia = lista_a_matriz(lista_adyacencia)
    elif opcion == 2:
        matriz_adyacencia = eval(input("Ingrese la matriz de adyacencia (por ejemplo, [[0, 1, 1], [1, 0, 0], [1, 0, 0]]): "))
        lista_adyacencia = matriz_a_lista(matriz_adyacencia)
    else:
        print("Opción no válida")
        return

    print("Representación en lista de adyacencia:")
    print(lista_adyacencia)
    print("Representación en matriz de adyacencia:")
    print(matriz_adyacencia)

    dibujar_grafo(lista_adyacencia)

if __name__ == "__main__":
    main()
