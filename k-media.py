#coding: utf-8

import sys

class Dado:
    def __init__(self, nome, d1, d2):
        self.nome = nome
        self.d1 = d1
        self.d2 = d2
        self.cluster = -1

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
    vetor[i].cluster =  c
    i += 1

# Inicializando variaveis para calculo de centroide
campo_d1 = [0, 0]
campo_d2 = [0, 0]
qtdd = [0, 0]

# Calculo de centroide
for i in range(len(vetor)):
    if vetor[i].cluster == 0:
        campo_d1[vetor[i].cluster] += vetor[i].d1
        campo_d2[vetor[i].cluster] += vetor[i].d2
        qtdd[0] += 1
    else:
        campo_d1[vetor[i].cluster] += vetor[i].d1
        campo_d2[vetor[i].cluster] += vetor[i].d2
        qtdd[1] += 1


campo_d1[0] = campo_d1[0] / qtdd[0]
campo_d2[0] = campo_d2[0] / qtdd[0]
campo_d1[1] = campo_d1[1] / qtdd[1]
campo_d2[1] = campo_d2[1] / qtdd[1]

print 'Centroide 1: (', campo_d1[0], ',', campo_d2[0], ')'
print 'Centroide 2: (', campo_d1[1], ',', campo_d2[1], ')'