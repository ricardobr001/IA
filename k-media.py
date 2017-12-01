#coding: utf-8

import sys
import math

class Dado:
    def __init__(self, nome, d1, d2):
        self.nome = nome
        self.d1 = d1
        self.d2 = d2
        self.cluster_atual = -1
        self.cluster_anterior = -1
        self.dist = []

vetor = []

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
# Lendo os dados do arquivo
for line1 in arquivo_cluster:
    nome = line1.split()[0]
    c = int(line1.split()[1])

    # Inserindo no vetor de dados
    vetor[i].cluster_atual =  c
    i += 1

# Inicializando variaveis para calculo de centroide
campo_d1 = [0, 0]
campo_d2 = [0, 0]
qtdd = [0, 0]
iteracao = 0

while True:
    # Soma para o calculo de centroide
    for i in range(len(vetor)):
        if vetor[i].cluster_atual == 0:
            campo_d1[vetor[i].cluster_atual] += vetor[i].d1
            campo_d2[vetor[i].cluster_atual] += vetor[i].d2
            qtdd[0] += 1
        else:
            campo_d1[vetor[i].cluster_atual] += vetor[i].d1
            campo_d2[vetor[i].cluster_atual] += vetor[i].d2
            qtdd[1] += 1

    # Calculando a média do centroide
    campo_d1[0] = campo_d1[0] / qtdd[0]
    campo_d2[0] = campo_d2[0] / qtdd[0]
    campo_d1[1] = campo_d1[1] / qtdd[1]
    campo_d2[1] = campo_d2[1] / qtdd[1]

    iteracao += 1
    print 'interação:', iteracao
    print 'Centroide 1: (', campo_d1[0], ',', campo_d2[0], ')'
    print 'Centroide 2: (', campo_d1[1], ',', campo_d2[1], ')'

    if iteracao == 1:
        # Calculando a distância euclidiana de cada objeto aos centroides
        for i in range(len(vetor)):
            vetor[i].dist.insert(len(vetor[i].dist), math.sqrt(math.pow(vetor[i].d1 - campo_d1[0], 2) + math.pow(vetor[i].d2 - campo_d2[0], 2)))
            vetor[i].dist.insert(len(vetor[i].dist), math.sqrt(math.pow(vetor[i].d1 - campo_d1[1], 2) + math.pow(vetor[i].d2 - campo_d2[1], 2)))
    else:
        for i in range(len(vetor)):
            vetor[i].dist[0] = math.sqrt(math.pow(vetor[i].d1 - campo_d1[0], 2) + math.pow(vetor[i].d2 - campo_d2[0], 2))
            vetor[i].dist[1] = math.sqrt(math.pow(vetor[i].d1 - campo_d1[1], 2) + math.pow(vetor[i].d2 - campo_d2[1], 2))

    # Associando cada objeto ao centroide mais próximo
    for i in range(len(vetor)):
        if vetor[i].dist[0] < vetor[i].dist[1]:     # A menor distância é para o primeiro centroide
            vetor[i].cluster_anterior, vetor[i].cluster_atual = vetor[i].cluster_atual, 0
        else:       # A menor distância é para o segundo centróide
            vetor[i].cluster_anterior, vetor[i].cluster_atual = vetor[i].cluster_atual, 1
    
    flag = False

    # Laço que verifica se algum objeto mudou de centroide
    for i in range(len(vetor)):
        if vetor[i].cluster_anterior != vetor[i].cluster_atual:     # Se mudou, marca a flag
            flag = True
            break
    
    if not flag:    # Se não houve mudança, para o algoritmo
        break