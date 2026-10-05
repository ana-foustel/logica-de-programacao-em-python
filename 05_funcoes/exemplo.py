#O que é uma função:

#Uma função é umm bloco de código criado para realizar uma determinada tarefa.
#Ela permite organizar e reutilizar código.

#1.Criando uma função
#utilizar a palavra def para uma função.

def saudacao():
    print("olá seja bem-vindo")

saudacao()

#2.Criando uma função com parâmetro

#parâmetros permitem enviar informações para a função.

def saudacao(nome):
    print(f"Ola {nome}")
saudacao("Ana")
saudacao("João")

#3. Mais de um parâmetro

def apresentar(nome, idade):
    print(f"nome: {nome}")
    print(f"idade: {idade}")

apresentar("Maria",17)
apresentar("joão",20)

#4 funcaocom calculo

def somar(numero1, numero2):
    resultado = numero1 + numero2
    print(f"resultado: {resultado}")

somar(10,20)

#5 Retornando um valor
#Return devolve um valor par ao local onde a função foi chamada

def somar(numero1, numero2):
    return numero1 + numero2

print(somar(10,5))

#6 Funcao com condição
def verificarIdade(idade):
    if idade >= 18:
        return "maior idade"

    else:
        return "menor idade"

print(verificarIdade(18))

#7 Parâmetro com valor padrão
def saudacao(nome = "Aluno"):
    print(f"Ola {nome}")

saudacao("João")

#8 Função utilizando lista

def calcularMedia(notas):
    soma = 0
    for nota in notas:
        soma += nota

    return soma/len(notas)
notas = [ 8, 7, 9, 10]
media = calcularMedia(notas)
print(f"media: {media}")

#9 Funções para organizar um programa

def cadastrar_produto():

    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    return nome, preco

def exibir_produto(nome, preco):

    print("\n====== PRODUTO ======")
    print(f"Nome: {nome}")
    print(f"Preco: R$ {preco:.2f}")

nome, preco = cadastrar_produto()
exibir_produto(nome, preco)

