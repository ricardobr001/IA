#coding: utf-8

import sys
import math
import time

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

if len(sys.argv) != 3:
    print 'MODO DE USAR: python k-media.py arquivo_dados.txt arquivo_clusters.clu'
    exit()

# Abrindo o arquivo passado pela linha de comando
try:
    arquivo_dados = open(sys.argv[1], 'r')
except IOError:
    print 'Erro!!'
    print 'Não foi possível abrir o arquivo (' + sys.argv[1] + ').'
    print '\n\nMODO DE USAR: python k-media.py arquivo_dados.txt arquivo_clusters.clu'    
    exit()

try:
    arquivo_cluster = open(sys.argv[2], 'r')
except IOError:
    print 'Erro!!'
    print 'Não foi possível abrir o arquivo (' + sys.argv[2] + ').'
    print '\n\nMODO DE USAR: python k-media.py arquivo_dados.txt arquivo_clusters.clu'    
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

i = 0
maior = 0
# Lendo os dados do arquivo
for line1 in arquivo_cluster:
    nome = line1.split()[0]
    c = int(line1.split()[1])

    if maior < c:
        maior = c

    # Inserindo no vetor de dados
    vetor[i].cluster_atual =  c
    i += 1

# Inicializando variaveis para calculo de centroide
for i in range(-1, maior):
    campo_d1.insert(len(campo_d1), 0)
    campo_d2.insert(len(campo_d2), 0)
    qtdd.insert(len(qtdd), 0)
    centroide.insert(len(centroide), [-1, -1])

iteracao = 0

while True:
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
            centroide[i][0], centroide[i][1] = -1, -11

    iteracao += 1
    print '\ninteração:', iteracao

    for i in range(len(centroide)):
        print 'Centroide', i,': (', centroide[i][0], ',', centroide[i][1], ')'

    if iteracao == 1:
        # Calculando a distância euclidiana de cada objeto aos centroides
        for i in range(len(vetor)):
            for j in range(len(centroide)):
                if centroide[j][0] != -1:
                    vetor[i].dist.insert(len(vetor[i].dist), math.sqrt(math.pow(vetor[i].d1 - centroide[j][0], 2) + math.pow(vetor[i].d2 - centroide[j][1], 2)))
    else:
        for i in range(len(vetor)):
            for j in range(len(centroide)):
                if centroide[j][0] != -1:
                    vetor[i].dist[j] = math.sqrt(math.pow(vetor[i].d1 - centroide[j][0], 2) + math.pow(vetor[i].d2 - centroide[j][1], 2))

    cluster_atual, cluster_anterior = 0, 0

    # Associando cada objeto ao centroide mais próximo
    for i in range(len(vetor)):
        menor_dist = 999

        for j in range(len(centroide)):
            if ((vetor[i].dist[j] < menor_dist) & (vetor[i].dist[j] > 0)):
                menor_dist, cluster_anterior, cluster_atual = vetor[i].dist[j], vetor[i].cluster_atual, j
        
        vetor[i].cluster_atual, vetor[i].cluster_anterior = cluster_atual, cluster_anterior
    
    flag = False

    # Laço que verifica se algum objeto mudou de centroide
    for i in range(len(vetor)):
        if vetor[i].cluster_anterior != vetor[i].cluster_atual:     # Se mudou, marca a flag
            flag = True
            break
    
    if not flag:    # Se não houve mudança, para o algoritmo
        break

    # Zerando variaveis para novo calculo
    for i in range(len(campo_d1)):
        campo_d1[i] = 0
        campo_d2[i] = 0
        qtdd[i] = 0