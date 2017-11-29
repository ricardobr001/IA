import sys

class Dado:
    def __init__(self, nome, d1, d2):
        self.nome = nome
        self.d1 = d1
        self.d2 = d2

vetor = []

# Abrindo o arquivo passado pela linha de comando
arquivo = open(sys.argv[1], 'r')

# Ignorando primeira linha do arquivo
arquivo.next()

# Lendo os dados do arquivo
for line in arquivo:
    nome = line.split()[0]
    d1 = float(line.split()[1])
    d2 = float(line.split()[2])

    # Inserindo no vetor de dados
    vetor.insert(len(vetor), Dado(nome, d1, d2))