#coding: utf-8

########################################################
# Nome: Leonardo Zaccarias              RA: 620491     #
# Nome: Ricardo Mendes Leal Junior      RA: 562262     #
# Nome: Vitor Pratali Camillo           RA: 620181     #
# Nome: Gabriel Peres de Andrade        RA: 726517     #
########################################################
import sys
import math

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

#Calcular distancia de um elemento para todos os elementos e inserindo no cluster
for i in range(len(cluster)):
    for j in range(len(vetor)):
        if i > j:
            pass
        else:
            cluster[i].dist.append(math.sqrt(math.pow(vetor[j].d1 - vetor[i].d1 , 2) + math.pow(vetor[j].d2 - vetor[i].d2 , 2)))
