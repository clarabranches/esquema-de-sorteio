import random
from time import sleep
item_aposta = ""
moedas = 100

def zero(valor):
    if(valor<=0):
        print("Você tem que fazer recarga")
        exit
    else:
        execute()


def jogar_novamente():
    jogar_novamente = int(input("Deseja jogar novamente? \n Digite 1 para SIM \n Digite 2 para Não\n"))
    if(jogar_novamente==1):
        zero(moedas)
    else:
        print("Foi um prazer ter você aqui, até mais tarde!!!")


def execute():
    global moedas
    global item_aposta

    def selecionar_ap():
        global item_aposta
        aposta = int(input("Digite \n 1 para apostar em cara. \n 2 para apostar em coroa. \n 3 para apostar no meio\n"))
        if aposta == 1:
            item_aposta = "cara"
        elif aposta == 2:
            item_aposta = "coroa"
        elif aposta == 3:
            item_aposta = "meio"
        else:
            selecionar_ap()
    
    
    #declarando vetores para realizar sorteio
    valores = ["cara","coroa","meio"]
    probabilidade = [0.40, 0.40, 0.20]
    r = [1,2]


    #interação com usuário informar saldo, selecionar aposta e valor de aposta
    print(f"Seu saldo é de {moedas} moeda(s)")
    sleep(3)
    aposta = ""
    selecionar_ap()

    valor_apostado = 999999999
    sleep(2)
    while(valor_apostado>moedas):
        valor_apostado = int(input("Digite o valor que você que apostar: "))
        if(valor_apostado>moedas):
            print(f"Seu saldo é de apenas {moedas} moedas\n")
    moedas = moedas - valor_apostado
    print(f"seu saldo atual é de {moedas}\n")

    #realizando sorteio para definir o item com maior probabilidade
    reoganizar = random.choice(r)
    if reoganizar == 1:
        probabilidade = [0.45, 0.35, 0.20]
    else:
        probabilidade = [0.35, 0.45, 0.20]

    #sorteio da moeda
    resultado = random.choices(valores, probabilidade)
    sleep(2)
    #exibir resultado
    print("Realizando Sorteio...")
    sleep(2)
    print(f"O resultado é: {resultado[0]}")

    sleep(2)
    if str(resultado[0])==item_aposta:
        print("Você Ganhou!!!!!")
        moedas = moedas +(valor_apostado*2)
        print(f"Seu saldo agora é de {moedas} moedas\n")
    else:
        print("Você Perdeu!")
        print(f"Seu saldo agora é de {moedas} moedas\n")

    jogar_novamente()

print("Olá, sejá bem vindo ao nosso programa de aposta")
execute()
