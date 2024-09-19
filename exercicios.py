
# QUESTÃO 1:
# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

# Segue o Exercicio

print('-'*30)
print("Sequência de Fibonacci")
print('-'*30)

numero = int(input("Quantos termos você quer que mostre? "))

t1 = 0
t2 = 1

encontrado = False

print('-'*30)
print('{} → {}'.format(t1, t2), end='')

if numero == t1 or numero == t2:
    encontrado = True

contador = 3
while contador <= numero:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')

    if t3 == numero:
        encontrado = True

    t1 = t2
    t2 = t3
    contador += 1

print(" → FIM.")
print('-'*30)

if encontrado:
    print(f"O número {numero} faz parte da Sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO faz parte da Sequência de Fibonacci.")



# QUESTÃO 2:
# Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
# IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código.git 

# Segue o Exercicio

print('-'*30)
print("Existência da letra 'A'")
print('-'*30)

texto = input("Digite uma string para verificar a existência da letra 'a': ")
quantidade = texto.count('a') + texto.count('A')
print('.'*30)

if quantidade > 0:
    print(f"A letra 'a' aparece {quantidade} vezes na string.")
else:
    print("A letra 'a' não aparece na string.")


# QUESTÃO 3:
# Observe o trecho de código abaixo: 
# int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?

# Segue o Exercicio

print('-'*30)
print("Cálculo da variável SOMA")
print('-'*30)

INDICE = 12
SOMA = 0
K = 1

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print('-'*30)
print(f"O valor final da variável SOMA é: {SOMA}")
print('-'*30)
