#Estrutura condicionais
nota = 6

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

#2. Condições com operadores lógicos
#and -> todas as condições devem ser verdadieras
#or -> pelo menos uma condição deve ser verdadeira
#not -> inverte o resultado

idade = 20
ingresso = True

if idade >= 18 and ingresso:
    print("Entrada permitida")
else:
    print("Entrada não permitida")

#3. Estrutura de Repetição

contador = 1

while contador <= 5:
    print(contador)
    contador += 1

#4. Estrutura de Repetição
for numero in range(1,6):
    print(numero)

#5. Percorrendo uma Lista
nomes = ["Ana", "Carlos", "João", "Maria"]

for nome in nomes:
    print(nome)

#6. Break

#0 brack interrompe completamente a repetição
#0 Pass nao executa nenhuma ação
#0 Continue interrompe apenas a repetição atual

for numero in range(1,11):
    if numero == 7:

        break
        pass
        continue

    print(numero)

#7. Condição dentro de repetição
for numero in range(1,11):
   if numero % 2 == 0:
       print(f"{numero} é par")

   else:
       print(f"{numero} é impar")