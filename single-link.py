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

#limpando distancias 
for i in range(len(cluster)):
    cluster[i].dist = []

for i in range(len(vetor)):
    cluster_final = [[i]]

inseridos = []

for i in range(len(menores_dist)):
    flag = False
    for j in range(len(cluster_final)):
        if menores_dist[i][1] in cluster_final[j] and menores_dist[i][2] in cluster_final[j]:   # Ambos já estão no mesmo cluster
            flag = True
            break
        elif menores_dist[i][1] in cluster_final[j]:    # Só o primeiro está no cluster
            cluster_final[j].append(menores_dist[i][2]) # Colocamos o segundo no cluster
            flag = True
            break
        elif menores_dist[i][2] in cluster_final[j]:    # Só o segundo está no cluster
            cluster_final[j].append(menores_dist[i][1]) # Colocamos o primeiro no cluster
            flag = True
            break

    if not flag:    # Se Não colocamos nenhum dos dois em nenhum cluster, eles são um novo cluster
        cluster_final.append([menores_dist[i][1], menores_dist[i][2]])        
            

# while len(cluster_final) != int(sys.argv[3]):
#     #juntar I E J
#     for j in range(len(menores_dist)):
#         # cluster[menores_dist[0][1]].dist.append(menores_dist[0][2])
#         pos, inserir = menores_dist[j][1], menores_dist[j][2]       # Para inserir no cluster
#         for k in range(len(cluster_final)):
#             # if menores_dist[0][1] == menores_dist[j][1]:
#             #     menores_dist[j][1] = menores_dist[0][1]
#             if in cluster_final[k]:  # Se ele estiver em algum cluster, marcamos a flag com True
#                 if k == pos:    # Se for a posição for a  que eu queria inserir
#                     break
#                 else:   # Se não
#                     pos = k     # Atualizamos a 
#                     break 

#         cluster[pos].dist.append(inserir)
    
#     for j in range(len(cluster)):
#         if not cluster[i].dist:  # Se o vetor estiver vazio
#             pass
#         else:   # Se tiver conteudo
#             cluster_final = cluster[i].dist     # Copia o conteudo para o final


#         print j
#         print 'cluster =', len(menores_dist)
#         del cluster[menores_dist[0][2]]
#         del menores_dist[0]
#         if j <= i:
#             break
        
    #remover o outro cluster
    # qtdd_dados -= 1

final = []
for i in range(len(cluster)):
    for j in range(len(cluster[i].dist)):
        final.append([vetor[cluster[i].dist[j]].nome, i]) # 

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