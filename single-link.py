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


cluster[] 
quantidade[]
vetor[] #objetos

qtdd_dados = 0

if len(sys.argv) != 5:
    print 'MODO DE USAR: python single-link.py <entrada.txt> <saida.clu> <quantidade_de_clusters> <quantidade_de_iterações>'
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
    cluster.append([Clust(qtdd_dados)])
    qtdd_dados += 1

#Aqui ja temos cada lugar de um Cluster como um Objeto

#Calcular distancia de um elemento para todos os elementos e inserindo no cluster
for i in range(len(cluster)):
    for j in range(len(vetor)):    
        if j > i:
            break
        else: 
            cluster[i].dist.append(math.sqrt(math.pow(vetor[j].d1 - vetor[i].d1 , 2) + math.pow(vetor[j].d2 - vetor[i].d2 , 2)))

# quais os Objetos mais pertos
menores_dist=[]
for i in range(len(cluster)):
    dist = 9999999999999
    k = False
    for j in range(len(cluster[i].dist)):
        if cluster[i].dist[j] < dist and i != j:
            dist = cluster[i].dist[j]
            if !k:
                menores_dist.insert(i,[cluster[i].dist[j], i, j])
                k = True
            else:
                menores_dist.[i] = [cluster[i].dist[j], i, j])

menores_dist = sorted(menores_dist,key=itemgetter(0))

#limpando distancias 
for i in range(len(cluster)):
    del cluster[1]

while qtdd_dados != int(sys.argv[3]):
    #juntar I E J
    cluster[menores_dist[0][1]].append(menores_dist[0][2])
     
    qtdd_dados -= 1
#achamos a menor distancia geral
# Junta o mais perto
# Atualiza a distancia desse Cluster aos outros
# Continua o Ciclo ate chegar a X interaçoes









