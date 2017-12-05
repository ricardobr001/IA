#coding: utf-8

########################################################
# Nome: Leonardo Zaccarias              RA: 620491     #
# Nome: Ricardo Mendes Leal Junior      RA: 562262     #
# Nome: Vitor Pratali Camillo           RA: 620181     #
# Nome: Gabriel Peres de Andrade        RA: 726517     #
########################################################

import sys
from sklearn import metrics

vetor_real = []         # Vetor com os clusters reais
vetor_calculado = []    # Vetor com os clusters calculado por determinado algoritmo

if len(sys.argv) != 3:
    print 'MODO DE USAR: <real.clu> <calculado.clu>'
    exit()

# Abrindo o arquivo passado pela linha de comando
try:
    real = open(sys.argv[1], 'r')
except IOError:
    print 'Erro!!'
    print 'Não foi possível abrir o arquivo (' + sys.argv[1] + ').'
    exit()

try:
    calculado = open(sys.argv[2], 'r')
except IOError:
    print 'Erro!!'
    print 'Não foi possível abrir o arquivo (' + sys.argv[2] + ').'
    exit()

# Lendo os dados do arquivo real
for line in real:
    vetor_real.insert(len(vetor_real), int(line.split()[1]))

# Lendo os dados do arquivo calculado
for line in calculado:
    vetor_calculado.insert(len(vetor_calculado), int(line.split()[1]))

res = metrics.adjusted_rand_score(vetor_real, vetor_calculado)

print 'Indice rand = %.4f' % (res)
