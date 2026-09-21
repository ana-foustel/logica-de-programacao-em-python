#Listas, Tuplas e Dicionários
from typing import cast

# 1. Listas
# Listas são utilizadas para armazenar varios valores dentro de uma variável.

nome = ["ana" , "Carlos" , "joão" , "Maria"]
print(nome)

# 2. Acessando Elementos da Lista
print(nome[1])

#podemos acessar o último elemento usando o -1
print(nome[-1])

#3. Alterando Elementos

nome[0] = "Pedro"
print(nome)
# 4. Adicionar Elementos

#append() adiciona um elemnto no final da Lista
nome.append("Lucas")
print(nome)

#insert() adiciona um elemento em uma posição especifica.
nome.insert(1,"Mariana")
print(nome)

# 5. Remove Elementos
#remove um elemento pelo valor

nome.pop(0)
print(nome)

# 6. Tamanho da Lista
#lend() informa quantidade d elementos

print(len(nome))

# 7. Percorrendo uma Lista
for nome in nome:
    print(nome)

# 8. Verificando se um elemento existe

if "joão" in nome:
    print("João esta na Lista")

else:
    print("João não esta na Lista")

# 9. Lista com diferentes tipos de dados
dados = ["João", 18, 1.75, True]
print(dados)

# 10. lista de números
notas = [7.5, 8.0, 6.5, 9.0]

soma = 0

for nota in notas:
    soma = soma + nota

media = soma/len(notas)
print(f"Média: {media}")

# 11. Tuplas
#Tuplas são semelhnates ás Listas.
# As tuplas não ser alteradas.

coordenadas = (10, 20)
print(coordenadas)

print(coordenadas[0])

# 12. Dicionarios

#Dicionarios armazenam informação no formato: chave: valor

aluno = {
    "nome": "Carlos",
    "Idade": 17,
    "nota1": 8.5
}

print(aluno)

