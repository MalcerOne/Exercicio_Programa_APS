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
          'estourar 21 pontos, você ganha também.\n'
          '--> As cartas denominadas "Ás" (A♦,A♠,A♥,A♣) valem 11 pontos. Porém,\n'
          'se sua mão estourar, e você tiver um "Ás", ele passa a valer 1 ponto.\n\n'
          'As recompensas são as seguintes:\n'
          '--> Ganhar com Blackjack: retorno da aposta, mais 150% do seu valor.\n'
          '--> Ganhar: retorno da aposta, mais 100% do seu valor.\n\n'
          "As regras do cassino são as seguintes:\n"
          "--> Não aposte o que você não tem em sua carteira. Erros são aceitos,\n"
          "mas se você repeti-los por mais de cinco vezes, os seguranças do cassino\n"
          "te chutam para fora.\n"
          "--> Quando você fica zerado, o jogo acaba, e boa sorte da próxima vez!\n"
          "Ah, claro, você pode digitar 'fim' a qualquer momento que quiser sair.\n"
          "--> Se divirta!")
intro()
# Criacao dos baralhos

baralho_base = ["A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥", "A♠", "2♠", "3♠", "4♠",
                "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠", "A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦",
                "9♦", "10♦", "J♦", "Q♦", "K♦", "A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣",
                "K♣"]
valor_cartas = {"A♥":11, "2♥":2, "3♥":3, "4♥":4, "5♥":5, "6♥":6, "7♥":7, "8♥":8, "9♥":9, "10♥":10, "J♥":10, "Q♥":10, "K♥":10, "A♠":11, "2♠":2, "3♠":3, "4♠":4,
                "5♠":5, "6♠":6, "7♠":7, "8♠":8, "9♠":9, "10♠":10, "J♠":10, "Q♠":10, "K♠":10, "A♦":11, "2♦":2, "3♦":3, "4♦":4, "5♦":5, "6♦":6, "7♦":7, "8♦":8,
                "9♦":9, "10♦":10, "J♦":10, "Q♦":10, "K♦":10, "A♣":11, "2♣":2, "3♣":3, "4♣":4, "5♣":5, "6♣":6, "7♣":7, "8♣":8, "9♣":9, "10♣":10, "J♣":10, "Q♣":10,
                "K♣":10}

# Dificuldade do jogo
dificuldade_jogo = input("Qual a dificuldade do jogo? (mf, f, m, d): ")

while dificuldade_jogo != "mf" and dificuldade_jogo != "f" and dificuldade_jogo != "m" and dificuldade_jogo != "d":
    print("Desculpe, dificuldade não encontrada. Tente de novo.")
    dificuldade_jogo = input("Qual a dificuldade do jogo? (mf, f, m, d): ")

# Conforme a dificuldade aumenta, a disponibilidade de cartas fica mais escassa.
if dificuldade_jogo == "mf":
    print("\n8 baralhos. Ridículo.")
    numero_de_baralhos = 8
elif dificuldade_jogo == "f":
    print("\n5 baralhos. Fácil. Dificuldade para se divertir.")
    numero_de_baralhos = 5
elif dificuldade_jogo == "m":
    print("\n3 baralhos. Boa escolha, preferiu a segurança ao risco.")
    numero_de_baralhos = 3
else:
    print("\n1 baralho. Boa sorte.")
    numero_de_baralhos = 1

# Recebe o quanto o jogador quer colocar na carteira.
carteira_string = input("Quanto você quer gastar de dinheiro? (essa será sua carteira de apostas): ")
carteira = carteira_string
while type(carteira)==type(carteira_string):
    try:
        carteira = float(carteira_string)
    except ValueError:
        print('\nTudo bem. Mas agora insira um número, por favor.')
        carteira_string = input("Quanto você quer gastar de dinheiro? (essa será sua carteira de apostas): ")
while carteira <= 0 or carteira > 1000000:
    if carteira <= 0:
        print('\nInsira um valor de dinheiro verdadeiro')
    else:
        print('\nO casino possui um limite de R$1.000.000 por participante')
    carteira_string = input("Quanto você quer gastar de dinheiro? (essa será sua carteira de apostas): ")
    carteira = carteira_string
    while type(carteira)==type(carteira_string):
        try:
            carteira = float(carteira_string)
        except ValueError:
            print('\nTudo bem. Mas agora insira um número, por favor.')
            carteira_string = input("Quanto você quer gastar de dinheiro? (essa será sua carteira de apostas): ")
# Loop do jogo.

#Parametros iniciais, definições de variáveis e listas.
i = True
contador_seguranca = 0

while i:
    aposta_string = input("Quanto você quer apostar nessa rodada? (Digite 'fim' para terminar o jogo): ")
    if aposta_string == "fim":
        print("\nObrigadx por jogar! Volte sempre!")
        break
    aposta_int = aposta_string
    while type(aposta_int) == type(aposta_string):
        try:
            aposta_int = float(aposta_string)
        except ValueError:
            aposta_int = 0
#Criacao do loop para limite de erros na aposta.
    while aposta_int > carteira or aposta_int <= 0:
        contador_seguranca += 1
        if contador_seguranca == 5:
            print("Nós avisamos. Os seguranças cuidarão de você.")
            i = False
            break
        if contador_seguranca == 4 and contador_seguranca != 5:
            print("\nVocê não pode fazer isso! Aposte de novo. Essa é sua última tentativa\n"
                  "antes de ser expulso da mesa. ")
            aposta_string = input("Quanto você quer apostar nessa rodada? (Digite 'fim' para terminar o jogo): ")
            if aposta_string == "fim":
                print("\nObrigadx por jogar! Volte sempre!")
                break
            aposta_int = aposta_string
            while type(aposta_int) == type(aposta_string):
                try:
                    aposta_int = float(aposta_string)
                except ValueError:
                    aposta_int = 0
            continue
        if contador_seguranca < 5:
            print("\nVocê não pode fazer isso! Aposte de novo. Você tem mais {0} tentativas\n"
                  "antes de ser expulso da mesa. ".format(5 - contador_seguranca))
            aposta_string = input("Quanto você quer apostar nessa rodada? (Digite 'fim' para terminar o jogo): ")
            if aposta_string == "fim":
                print("\nObrigadx por jogar! Volte sempre!")
                break
            aposta_int = aposta_string
            while type(aposta_int) == type(aposta_string):
                try:
                    aposta_int = float(aposta_string)
                except ValueError:
                    aposta_int = 0
    if aposta_string == "fim":
        break
    carteira -= aposta_int
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
#Computador dá as duas cartas do topo do monte para o jogador
    mao_jogador = monte[0:2].copy()
    del monte[0:2]
    print ('\nSuas cartas são {0}.'.format(mao_jogador))
    contador_as=0
    for carta in mao_jogador:
        if carta == 'A♥' or carta == 'A♠' or carta == 'A♦' or carta == 'A♣':
            contador_as+=1
    valor_mao = valor_cartas[mao_jogador[0]] + valor_cartas[mao_jogador[1]]
    if valor_mao > 21:
        valor_mao -= 10
        contador_as -= 1
#chacando se há blackjack
    if valor_mao == 21:
        carteira+=2.5*aposta_int
        print('BLACKJACK!!!\nVocê ganhou R${0}.\nSaldo atual: R${1}.'.format(2.5*aposta_int,carteira))
        continue
#se não há blackjack, jogador escolhe sua ação
    print('Você está com {0} pontos. O que deseja fazer?'.format(valor_mao))
    escolha=input('Digite "mais uma" para mais cartas.\nPressione apenas "Enter" para concluir sua rodada: ')
    while escolha != 'mais uma' and escolha != '':
        print('\nJogada inválida. Agora que começou a rodada, vá até o fim.')
        escolha=input('Digite "mais uma" para mais cartas.\nPressione apenas "Enter" para concluir sua rodada: ')
    indice_carta_mao=1
    while escolha == 'mais uma':
        indice_carta_mao+=1
        mao_jogador.append(monte[0])
        if monte[0]=='A♥' or monte[0] == 'A♠' or monte[0] == 'A♦' or monte[0] == 'A♣':
            contador_as+=1
        del monte[0]
        valor_mao+=valor_cartas[mao_jogador[indice_carta_mao]]
        if valor_mao == 21:
            break
        if valor_mao > 21:
            if contador_as > 0:
                valor_mao -= 10
                contador_as -= 1
                print('\nSua mão estava estourada, então seu Ás passa a valer 1 ponto.')
            else:
                break
        print ('\nSuas cartas são {0}.'.format(mao_jogador))
        print('Você está com {0} pontos. O que deseja fazer?'.format(valor_mao))
        escolha=input('Digite "mais uma" para mais cartas.\nPressione apenas "Enter" para concluir sua rodada: ')
        while escolha != 'mais uma' and escolha != '':
            print('Jogada inválida. Agora que começou a rodada, vá até o fim.')
            escolha=input('Digite "mais uma" para mais cartas.\nPressione apenas "Enter" para concluir sua rodada: ')
#jogo para porque jogador consegue 21
    if valor_mao == 21:
        carteira+=2.5*aposta_int
        print ('\nSuas cartas são {0}.'.format(mao_jogador))
        print('BLACKJACK!!!\nVocê ganhou R${0}.\nSaldo atual: R${1}.'.format(2.5*aposta_int,carteira))
#jogo para porque jogador ultrapassou 21
    elif valor_mao > 21:
        print ('\nSuas cartas são {0}.'.format(mao_jogador))
        print('Você está com {0} pontos.'.format(valor_mao))
        print('Você ultrapassou 21 pontos, e perdeu sua aposta.\nSaldo atual: R${0}.'.format(carteira))
        if carteira == 0:
            print('\nSua carteira está vazia.\nParece que hoje não era seu dia de sorte...\nObrigadx por jogar! Volte sempre!')
            i = False
#jogo para porque jogador pediu
#aqui inicia o loop da banca
    else:
        cartas_banca = monte[0:2].copy()
        del monte[0:2]
        contador_as=0
        for carta in cartas_banca:
            if carta == 'A♥' or carta == 'A♠' or carta == 'A♦' or carta == 'A♣':
                contador_as+=1
        valor_banca = valor_cartas[cartas_banca[0]] + valor_cartas[cartas_banca[1]]
        if valor_banca > 21:
            valor_banca -= 10
            contador_as -= 1
#blackjack da banca
        if valor_banca == 21 or valor_banca > valor_mao or (valor_banca >= 17 and valor_banca == valor_mao) or (valor_mao > valor_banca and valor_banca >= 17):
            oi=0
#banca com menos de 17 pontos
        else:
            print('\nSuas cartas: {0}\nSeus pontos: {1}\nCartas da banca: {2}\nPontos da banca: {3}'.format(mao_jogador,valor_mao,cartas_banca,valor_banca))
            input('Pressione "Enter" para continuar.')
        indice_carta_banca = 1
        while valor_banca <= valor_mao and valor_banca < 17:
            indice_carta_banca+=1
            cartas_banca.append(monte[0])
            if monte[0]=='A♥' or monte[0] == 'A♠' or monte[0] == 'A♦' or monte[0] == 'A♣':
                contador_as+=1
            del monte[0]
            valor_banca += valor_cartas[cartas_banca[indice_carta_banca]]
#banca ultrapassou 21 pontos
            if valor_banca > 21:
                if contador_as > 0:
                    valor_banca -= 10
                    contador_as -= 1
                else:
                    break
            elif valor_banca > valor_mao:
                break
            print('Suas cartas: {0}\nSeus pontos: {1}\nCartas da banca: {2}\nPontos da banca: {3}'.format(mao_jogador,valor_mao,cartas_banca,valor_banca))
            input('Pressione "Enter" para continuar.')
#mensagens finais:
#banca ganha com 21
        if valor_banca == 21:
            print('\nÉ Blackjack para a banca... que azar para você.')
            print('Suas cartas: {0}\nSeus pontos: {1}\nCartas da banca: {2}\nPontos da banca: {3}'.format(mao_jogador,valor_mao,cartas_banca,valor_banca))
            if valor_banca-valor_mao != 1:
                print('A banca ganhou, por {0} pontos.\nSaldo atual: R${1}.'.format(valor_banca-valor_mao,carteira))
            else:
                print('A banca ganhou, por 1 ponto.\nSaldo atual: R${0}.'.format(carteira))
#banca ultrapassa 21
        elif valor_banca > 21:
            carteira += 2*aposta_int
            print('\nSuas cartas: {0}\nSeus pontos: {1}\nCartas da banca: {2}\nPontos da banca: {3}'.format(mao_jogador,valor_mao,cartas_banca,valor_banca))
            print('A banca ultrapassou 21 pontos.\nVocê ganhou R${0}!\nSaldo atual: {1}.'.format(2*aposta_int,carteira))
#banca ganha
        elif valor_banca > valor_mao:
            print('\nSuas cartas: {0}\nSeus pontos: {1}\nCartas da banca: {2}\nPontos da banca: {3}'.format(mao_jogador,valor_mao,cartas_banca,valor_banca))
            if valor_banca - valor_mao != 1:
                print('A banca ganhou, por {0} pontos.\nSaldo atual: R${1}.'.format(valor_banca-valor_mao,carteira))
            else:
                print('A banca ganhou, por 1 ponto.\nSaldo atual: R${0}.'.format(carteira))
#jogador ganha
        elif valor_mao > valor_banca:
            carteira += 2*aposta_int
            print('\nSuas cartas: {0}\nSeus pontos: {1}\nCartas da banca: {2}\nPontos da banca: {3}'.format(mao_jogador,valor_mao,cartas_banca,valor_banca))
            if valor_mao-valor_banca != 1:
                print('Você ganhou por {0} pontos!\nParabéns, você recebeu R${1}!\nSaldo atual: R${2}'.format(valor_mao-valor_banca, 2*aposta_int, carteira))
            else:
                print('Você ganhou por 1 ponto!\nParabéns, você recebeu R${0}!\nSaldo atual: R${1}'.format(2*aposta_int, carteira))
#empate
        elif valor_banca == valor_mao:
            carteira += aposta_int
            print('\nSuas cartas: {0}\nSeus pontos: {1}\nCartas da banca: {2}\nPontos da banca: {3}'.format(mao_jogador,valor_mao,cartas_banca,valor_banca))
            print('É um empate! Você recebe sua aposta de volta.\nSaldo atual: {0}'.format(carteira))
#verifica se o jogador ainda tem saldo
        if carteira == 0:
            print('\nSua carteira está vazia.\nParece que hoje não era seu dia de sorte...\nObrigadx por jogar! Volte sempre!')
            i = False
