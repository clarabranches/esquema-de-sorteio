import random
from time import sleep

#declarando vetores para realizar sorteio
valores = ["cara","coroa","meio"]
probabilidade = [0.40, 0.40, 0.20]
r = [1,2]

#interação com usuário informar saldo, selecionar aposta e valor de aposta
print("Olá, sejá bem vindo ao nosso programa de aposta \n Você resceu um saldo de 100 moedas")
moedas = 100
sleep(5)
aposta = input("Digite \n 1 para apostar em cara. \n 2 para apostar em coroa. \n 3 para apostar no meio\n")
if aposta == 1:
    aposta = "cara"
elif aposta == 2:
    aposta = "coroa"
else:
    aposta = "meio"

valor_apostado = 102

while(valor_apostado>100):
    valor_apostado = int(input("Digite o valor que você que apostar: "))
    if(valor_apostado>100):
        print("Seu saldo é de apenas 100 moedas")
moedas = moedas - valor_apostado
print(f"seu saldo atual é de {moedas}")

#realizando sorteio para definir o item com maior probabilidade
reoganizar = random.choice(r)
if reoganizar == 1:
    probabilidade = [0.45, 0.35, 0.20]
else:
    probabilidade = [0.35, 0.45, 0.20]

#sorteio da moeda
resultado = random.choices(valores, probabilidade)

#exibir resultado
print(resultado[0])


if resultado[0]==aposta:
    print("Você Ganhou!!!!!")
    moedas = moedas +(valor_apostado*2)
    print(f"Seu saldo agora é de {moedas} moedas")
else:
    print("Você Perdeu!")
    print(f"Seu saldo agora é de {moedas} moedas")