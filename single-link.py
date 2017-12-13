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
from operator import itemgetter
# Definindo o objeto Dado
class Dado:
    def __init__(self, nome, d1, d2):
        self.nome = nome
        self.d1 = d1
        self.d2 = d2

class Clust:
    def __init__(self,vet):
        self.vet = vet
        self.dist = []

def find(x):
    global cluster_final

    if cluster_final[x][0] != x:
        cluster_final[x][0] = find(cluster_final[x][0])
    return cluster_final[x][0]

def union(x, y):
    global cluster_final

    raizX_pai = find(x)
    raizY_pai = find(y)

    if raizX_pai == raizY_pai:  # Se os dois estiverem no mesmo cluster (mesmos pais)
        return  # Sai sem fazer nada

    if cluster_final[raizX_pai][1] < cluster_final[raizY_pai][1]:   # Se nnão estiverem no mesmo nível, unimos eles
        cluster_final[raizX_pai][0] = raizY_pai
    elif cluster_final[raizX_pai][1] > cluster_final[raizY_pai][1]:
        cluster_final[raizY_pai][0] = raizX_pai
    else:
        cluster_final[raizY_pai][0] = raizX_pai
        cluster_final[raizX_pai][1] += 1

def qtdd_pais(vet):
    global pais

    pais = []
    for i in range(len(vet)):
        if vet[i][0] in pais:
            pass
        else:
            pais.append(vet[i][0])
    return len(pais)


cluster = []
quantidade = []
vetor = [] #objetos

qtdd_dados = 0

if len(sys.argv) != 4:
    print 'MODO DE USAR: python single-link.py <entrada.txt> <saida.clu> <quantidade_de_clusters>'
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

#Aqui ja temos cada lugar de um Cluster como um Objeto

#Calcular distancia de um elemento para todos os elementos e inserindo no cluster
for i in range(len(cluster)):
    for j in range(len(vetor)):
        if i > j:
            pass
        else:
            cluster[i].dist.append(math.sqrt(math.pow(vetor[j].d1 - vetor[i].d1 , 2) + math.pow(vetor[j].d2 - vetor[i].d2 , 2)))

# quais os Objetos mais pertos
menores_dist = []
for i in range(len(cluster)):
    dist = 9999999999999
    k = False
    for j in range(len(cluster[i].dist)):
        if cluster[i].dist[j] < dist and j != 0:
            dist = cluster[i].dist[j]
            if not k:
                menores_dist.insert(i,[cluster[i].dist[j], i, j])
                k = True
            else:
                menores_dist[i] = [cluster[i].dist[j], i, j]

menores_dist = sorted(menores_dist, key=itemgetter(0))

cluster_final = []
for i in range(len(vetor)):
    cluster_final.append([i, 0])    # Todo cara é seu próprio pai e está no nível 0

# while qtdd_pais(cluster_final) != int(sys.argv[3]):   # Enquanto não chegar na quantidade desejada de clusters
pais = []
for i in range(len(menores_dist)):
    union(menores_dist[i][1], menores_dist[i][2])

    if qtdd_pais(cluster_final) == int(sys.argv[3]):    # Se chagar na quantidade desejada de cluster, para!
            break

pais = sorted(pais)
final = []
for i in range(len(cluster_final)):
    final.append([vetor[i].nome, pais.index(cluster_final[i][0])]) #

final = sorted(final, key=itemgetter(0))

# Abrindo arquivo de saida
arquivo_saida = open(sys.argv[2], 'w')

# Imprimindo resultados no arquivo
for i in range(len(final)):
    arquivo_saida.write(final[i][0] + ' ' + str(final[i][1]) + '\n')
#achamos a menor distancia geral
# Junta o mais perto
# Atualiza a distancia desse Cluster aos outros
# Continua o Ciclo ate chegar a X interaçoes
