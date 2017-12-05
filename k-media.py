#coding: utf-8

########################################################
# Nome: Leonardo Zaccarias              RA: 620491     #
# Nome: Ricardo Mendes Leal Junior      RA: 562262     #
# Nome: Vitor Pratali Camillo           RA: 620181     #
# Nome: Gabriel Peres de Andrade        RA: 726517     #
########################################################

import sys
import math
import random

# Definindo o objeto Dado
class Dado:
    def __init__(self, nome, d1, d2):
        self.nome = nome
        self.d1 = d1
        self.d2 = d2
        self.cluster_atual = -1
        self.cluster_anterior = -1
        self.dist = []

# Declaração dos vetores
vetor = []      # Vetor com os objetos do tipo Dado
campo_d1 = []   # Vetor compo d1
campo_d2 = []   # Vetor campo d2
qtdd = []       # Vetor da quantidade
centroide = []  # Vetor dos centroides
qtdd_dados = 0

if len(sys.argv) != 5:
    print 'MODO DE USAR: python k-media.py <entrada.txt> <saida.clu> <quantidade_de_centroides> <quantidade_de_iterações>'
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
    qtdd_dados += 1

    # Inserindo no vetor de dados
    vetor.insert(len(vetor), Dado(nome, d1, d2))

# Inicializando variaveis para calculo de centroide
for i in range(0, int(sys.argv[3])):
    j = random.randint(0, qtdd_dados)   # Rand para escolher os centroides aleatoriamente
    campo_d1.insert(len(campo_d1), 0)
    campo_d2.insert(len(campo_d2), 0)
    qtdd.insert(len(qtdd), 0)
    centroide.insert(len(centroide), [vetor[j].d1, vetor[j].d2])

iteracao = 0

while iteracao < int(sys.argv[4]):
    if iteracao == 0:
        # Calculando a distância euclidiana de cada objeto aos centroides
        for i in range(len(vetor)):
            for j in range(len(centroide)):
                vetor[i].dist.insert(len(vetor[i].dist), math.sqrt(math.pow(vetor[i].d1 - centroide[j][0], 2) + math.pow(vetor[i].d2 - centroide[j][1], 2)))
    else:
        for i in range(len(vetor)):
            for j in range(len(centroide)):
                vetor[i].dist[j] = math.sqrt(math.pow(vetor[i].d1 - centroide[j][0], 2) + math.pow(vetor[i].d2 - centroide[j][1], 2))

    cluster_atual, cluster_anterior = 0, 0

    # Associando cada objeto ao centroide mais próximo
    for i in range(len(vetor)):
        menor_dist = 999

        for j in range(len(centroide)):
            if ((vetor[i].dist[j] < menor_dist) & (vetor[i].dist[j] > 0)):
                menor_dist, cluster_anterior, cluster_atual = vetor[i].dist[j], vetor[i].cluster_atual, j

        vetor[i].cluster_atual, vetor[i].cluster_anterior = cluster_atual, cluster_anterior

    # Soma para o calculo de centroide
    for i in range(len(vetor)):
        campo_d1[vetor[i].cluster_atual] += vetor[i].d1
        campo_d2[vetor[i].cluster_atual] += vetor[i].d2
        qtdd[vetor[i].cluster_atual] += 1

    # Calculando a média do centroide
    for i in range(len(qtdd)):
        if qtdd[i] != 0:
            centroide[i][0], centroide[i][1] = (campo_d1[i] / qtdd[i]), (campo_d2[i] / qtdd[i])
        else:
            centroide[i][0], centroide[i][1] = -1, -1

    iteracao += 1

    # Zerando variaveis para novo calculo
    for i in range(len(campo_d1)):
        campo_d1[i] = 0
        campo_d2[i] = 0
        qtdd[i] = 0

# Abrindo arquivo de saida
arquivo_saida = open(sys.argv[2], 'w')

# Imprimindo resultados no arquivo
for i in range(len(vetor)):
    arquivo_saida.write(vetor[i].nome + ' ' + str(vetor[i].cluster_atual) + '\n')
