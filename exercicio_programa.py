import random
#Introducao do jogo para os players, alem de mostrar as regras do mesmo.
def intro():
    print("♠♣ Bem vindo ao Blackjack! ♥♦\n"
          "Aproxime-se e veja se você consegue\n"
          "ganhar do dealer e chegar o mais perto de 21 possível sem estourar!\n\n"
          "As regras do Blackjack são as seguintes:\n"
          '--> O dealer te entrega duas cartas. Se a soma delas for exatamente 21,\n'
          'é Blackjack, e você ganha automaticamente!'
          "--> Se não há Blackjack, você tem duas opções:\n"
          '    --> Parar o jogo com as cartas que possui\n'
          '    --> Pedir mais cartas, uma por vez, até decidir parar o jogo\n'
          '--> Se a soma de suas cartas for maior que 21, você perde automaticamente\n'
          '--> Se você ainda está no jogo, suas cartas são comparadas com a do dealer,\n'
          'e quem estiver mais próximo de 21 ganha a rodada. Se o dealer estourar 21/n'
          'pontos, você ganha também.\n\n'
          'As recompensas são as seguintes:\n'
          '--> Ganhar com Blackjack: retorno da aposta, mais 150% do seu valor\n'
          '--> Ganhar: retorno da aposta, mais 100% do seu valor\n\n'
          "As regras do casino são as seguintes:\n"
          "--> Não aposte o que você não tem em sua carteira. Erros são aceitos,\n"
          "mas se você repeti-los por mais de cinco vezes, os seguranças do cassino\n"
          "te chutam para fora.\n"
          "--> Quando você fica zerado, o jogo acaba, e boa sorte da próxima vez!\n"
          "Ah, claro, você pode digitar 'fim' a qualquer momento que quiser sair.\n"
          "--> Se divirta!")

#Criacao dos baralhos
#Naipes
naipe_paus = ["Ap", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "Jp", "Qp", "Kp"]
naipe_copas = ["Ac", "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "10c", "Jc", "Qc", "Kc"]
naipe_espadas = ["Ae", "2e", "3e", "4e", "5e", "6e", "7e", "8e", "9e", "10e", "Je", "Qe", "Ke"]
naipe_ouros = ["Ao", "2o", "3o", "4o", "5o", "6o", "7o", "8o", "9o", "10o", "Jo", "Qo", "Ko"]

baralho = [naipe_copas, naipe_espadas, naipe_ouros, naipe_paus]

carteira  = int(input("Quanto você quer gastar de dinheiro? (essa será sua carteira de apostas): "))
while carteira <=0 or carteira>1000000:
    if carteira<=0:
        print('Insira um valor de dinheiro verdadeiro')
    else:
        print('O casino possui um limite de R$1.000.000 por participante')
    carteira  = int(input("Quanto você quer gastar de dinheiro? (essa será sua carteira de apostas): "))
    
i = True
while i:
    aposta = int(input("Quanto você quer apostar?: "))
    if aposta == "fim":
        print("Obrigado por jogar! Volte sempre!")
        break
    contador_seguranca = 0
    while aposta > carteira or aposta <= 0:
        contador_seguranca += 1
        print("Você não tem esse dinheiro! Aposte de novo. Você tem mais {0} tentativas\n"
              "antes de ser expulso da mesa. ".format(5-contador_seguranca))
        aposta = int(input("Quanto você quer apostar?: "))
