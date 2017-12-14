#coding: utf-8

########################################################
# Nome: Leonardo Zaccarias              RA: 620491     #
# Nome: Ricardo Mendes Leal Junior      RA: 562262     #
# Nome: Vitor Pratali Camillo           RA: 620181     #
# Nome: Gabriel Peres de Andrade        RA: 726517     #
########################################################

import sys
import math
import numpy as np

class Dado:
    def __init__(self, nome, d1, d2):
        self.nome = nome
        self.d1 = d1
        self.d2 = d2

class Clust:
    def __init__(self, vet):
        self.vet = vet
        self.grupo = [vet]

def crie_matriz(n_linhas, n_colunas, valor):
    ''' (int, int, valor) -> matriz (lista de listas)

    Cria e retorna uma matriz com n_linhas linha e n_colunas
    colunas em que cada elemento é igual ao valor dado.
    '''

    matriz = [] # lista vazia
    for i in range(n_linhas):
        # cria a linha i
        linha = [] # lista vazia
        for j in range(n_colunas):
            linha.append(valor)

        # coloque linha na matriz
        matriz.append(linha)

    return matriz

cluster = []
quantidade = []
vetor = [] #objetos

qtdd_dados = 0

if len(sys.argv) != 4:
    print 'MODO DE USAR: python average-link.py <entrada.txt> <saida.clu> <quantidade_de_clusters>'
    exit()


# Abrindo o arquivo passado pela linha de comando
try:
    arquivo_dados = open(sys.argv[1], 'r')
except IOError:
    print 'Erro!!'
    print 'Não foi possível abrir o arquivo (' + sys.argv[1] + ').'
    exit()

# Ignorando primeira linha do arquivo
arquivo_dados.next()

# Lendo os dados do arquivo
for line in arquivo_dados:
    nome = line.split()[0]
    d1 = float(line.split()[1])
    d2 = float(line.split()[2])
    # Inserindo no vetor de dados
    vetor.insert(len(vetor), Dado(nome, d1, d2))
    cluster.append(Clust(qtdd_dados))
    qtdd_dados += 1

matriz_dist = crie_matriz(qtdd_dados, qtdd_dados, -1)

#Calcular distancia de um elemento para todos os elementos e inserindo no cluster
for i in range(len(matriz_dist)):
    for j in range(len(matriz_dist[i])):
        if i > j:
            pass
        else:
            matriz_dist[i][j] = math.sqrt(math.pow(vetor[j].d1 - vetor[i].d1 , 2) + math.pow(vetor[j].d2 - vetor[i].d2 , 2))

# a = open('teste.txt', 'w')
# for i in range(len(cluster)):
#     for j in range(len(cluster[i].dist)):
#         a.write(str(cluster[i].dist[j]) + '\t')
#     a.write('\n')

while len(matriz_dist) != int(sys.argv[3]):
    menor = 999999999
    for i in range(len(matriz_dist)):
        for j in range(len(matriz_dist[i])):
            if matriz_dist[i][j] < menor and j != i and matriz_dist[i][j] != -1:
                menor, a, b = matriz_dist[i][j], i, j

    # 'a' linha, 'b' coluna
    cluster[b].grupo.append(a)  # Agrupando a com b
    cluster[a].grupo.append(b)

    # Diminui uma coluna
    for i in range(len(matriz_dist)):
        del matriz_dist[i][b]

    del matriz_dist[a]          # Diminui uma linha

    # Recalculando a coluna
    for i in range(len(matriz_dist)):
        matriz_dist[i][b] = 0
        for j in range(len(cluster[b].grupo)):
            matriz_dist[i][b] += math.sqrt(math.pow(vetor[i].d1 - vetor[cluster[b].grupo[j]].d1, 2) + math.pow(vetor[i].d2 - vetor[cluster[b].grupo[j]].d2, 2))

        matriz_dist[i][b] = matriz_dist[i][b] / len(cluster[b].grupo) # Divide pelo total de objetos no cluster

    # Recalculando a linha
    for i in range(len(matriz_dist[a])):
        matriz_dist[a][i] = 0
        for j in range(len(cluster[a].grupo)):
            matriz_dist[a][i] += math.sqrt(math.pow(vetor[i].d1 - vetor[cluster[a].grupo[j]].d1, 2) + math.pow(vetor[i].d2 - vetor[cluster[a].grupo[j]].d2, 2))

        matriz_dist[a][i] = matriz_dist[a][i] / len(cluster[a].grupo)

    print 'Temos %d clusters!' % (len(matriz_dist))
