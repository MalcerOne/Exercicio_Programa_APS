import random


# Introducao do jogo para os players, alem de mostrar as regras do mesmo.
def intro():
    print("♠♣ Bem vindo ao Blackjack! ♥♦\n"
          "Aproxime-se e veja se você consegue ganhar do dealer e chegar o mais\n"
          "perto de 21 possível sem estourar!\n\n"
          "As regras do Blackjack são as seguintes:\n"
          '--> O dealer te entrega duas cartas. Se a soma delas for exatamente\n'
          '21, é Blackjack, e você ganha automaticamente!\n'
          "--> Se não há Blackjack, você tem duas opções:\n"
          '    --> Parar o jogo com as cartas que possui\n'
          '    --> Pedir mais cartas, uma por vez, até decidir parar o jogo\n'
          '--> Se a soma de suas cartas for maior que 21, você perde na hora\n'
          '--> Se você ainda está no jogo, suas cartas são comparadas com a do\n'
          'dealer, e quem estiver mais próximo de 21 ganha a rodada. Se o dealer\n'
          'estourar 21 pontos, você ganha também.\n\n'
          'As recompensas são as seguintes:\n'
          '--> Ganhar com Blackjack: retorno da aposta, mais 150% do seu valor.\n'
          '--> Ganhar: retorno da aposta, mais 100% do seu valor.\n\n'
          "As regras do casino são as seguintes:\n"
          "--> Não aposte o que você não tem em sua carteira. Erros são aceitos,\n"
          "mas se você repeti-los por mais de cinco vezes, os seguranças do cassino\n"
          "te chutam para fora.\n"
          "--> Quando você fica zerado, o jogo acaba, e boa sorte da próxima vez!\n"
          "Ah, claro, você pode digitar 'fim' a qualquer momento que quiser sair.\n"
          "--> Se divirta!")
intro()
# Criacao dos baralhos

baralho_base = ["Ac", "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "10c", "Jc", "Qc", "Kc", "Ae", "2e", "3e", "4e",
                "5e", "6e", "7e", "8e", "9e", "10e", "Je", "Qe", "Ke", "Ao", "2o", "3o", "4o", "5o", "6o", "7o", "8o",
                "9o", "10o", "Jo", "Qo", "Ko", "Ap", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "Jp", "Qp",
                "Kp"]

# Dificuldade do jogo
dificuldade_jogo = input("Qual a dificuldade do jogo? (mf, f, m, d): ")

while dificuldade_jogo != "mf" and dificuldade_jogo != "f" and dificuldade_jogo != "m" and dificuldade_jogo != "d":
    print("Desculpe, dificuldade não encontrada. Tente de novo.")
    dificuldade_jogo = input("Qual a dificuldade do jogo? (mf, f, m, d): ")

# Conforme a dificuldade aumenta, a disponibilidade de cartas fica mais escassa.
if dificuldade_jogo == "mf":
    print("Ridículo.")
    numero_de_baralhos = 10
elif dificuldade_jogo == "f":
    print("Fácil. Dificuldade para se divertir.")
    numero_de_baralhos = 6
elif dificuldade_jogo == "m":
    print("Boa escolha, preferiu a segurança ao risco.")
    numero_de_baralhos = 3
elif dificuldade_jogo == "d":
    print("Boa sorte.")
    numero_de_baralhos = 1

# Recebe o quanto o jogador quer colocar na carteira.
carteira = int(input("Quanto você quer gastar de dinheiro? (essa será sua carteira de apostas): "))
while carteira <= 0 or carteira > 1000000:
    if carteira <= 0:
        print('Insira um valor de dinheiro verdadeiro')
    else:
        print('O casino possui um limite de R$1.000.000 por participante')
    carteira = int(input("Quanto você quer gastar de dinheiro? (essa será sua carteira de apostas): "))

# Loop do jogo.

#Parametros iniciais, definições de variáveis e listas.
i = True
contador_seguranca = 0

while i:
    aposta_string = input("Quanto você quer apostar?: ")
    if aposta_string == "fim":
        print("Obrigado por jogar! Volte sempre!")
        break
    aposta_int = int(aposta_string)
#Criacao do loop para limite de erros na aposta.
    while aposta_int > carteira or aposta_int <= 0:
        contador_seguranca += 1
        if contador_seguranca == 5:
            print("Nós avisamos. Os seguranças cuidarão de você.")
            i = False
            break
        if contador_seguranca == 4 and contador_seguranca != 5:
            print("Você não tem esse dinheiro! Aposte de novo. Essa é sua última tentativa\n"
                  "antes de ser expulso da mesa. ")
            aposta_int = int(input("Quanto você quer apostar?: "))
            continue
        if contador_seguranca < 5:
            print("Você não tem esse dinheiro! Aposte de novo. Você tem mais {0} tentativas\n"
                  "antes de ser expulso da mesa. ".format(5 - contador_seguranca))
            aposta_int = int(input("Quanto você quer apostar?: "))
# Embaralhando as cartas.
    baralho = []
    for t in range(0, numero_de_baralhos):
        for a in range(len(baralho_base)):
            baralho.append(baralho_base[a])
    monte = []
    quantidade_de_cartas = len(baralho)
    while quantidade_de_cartas != 0:
        carta = baralho[random.randint(0, quantidade_de_cartas - 1)]
        monte.append(carta)
        indice_da_carta = 0
        while indice_da_carta < quantidade_de_cartas:
            if carta == baralho[indice_da_carta]:
                del baralho[indice_da_carta]
                break
            indice_da_carta += 1
        quantidade_de_cartas -= 1
