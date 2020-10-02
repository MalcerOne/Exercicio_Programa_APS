import random


# Introdução do jogo para os players, alem de mostrar as regras do mesmo.
def intro():
    print("\n♠♣ Bem vindo ao Blackjack! ♥♦"
          "\nAproxime-se e veja se você consegue ganhar do dealer e chegar o mais"
          "\nperto de 21 possível sem estourar!"
          "\n\nAs regras do Blackjack são as seguintes:"
          '\n--> O dealer te entrega duas cartas. Se a soma delas for exatamente'
          '\n21, é Blackjack, e você ganha automaticamente!'
          "\n--> Se não há Blackjack, você tem duas opções:"
          '\n    --> Parar o jogo com as cartas que possui;'
          '\n    --> Pedir mais cartas, uma por vez, até decidir parar o jogo.'
          '\n--> Se a soma de suas cartas for maior que 21, você perde na hora.'
          '\n--> Se você ainda está no jogo, suas cartas são comparadas com a do'
          '\ndealer, e quem estiver mais próximo de 21 ganha a rodada. Se o dealer'
          '\nestourar 21 pontos, você ganha também.'
          '\n--> As cartas denominadas "Ás" (A♦,A♠,A♥,A♣) valem 11 pontos. Porém,'
          '\nse sua mão estourar, e você tiver um "Ás", ele passa a valer 1 ponto.'
          '\n\nAs recompensas são as seguintes:'
          '\n--> Ganhar com Blackjack: retorno da aposta, mais 150% do seu valor.'
          '\n--> Ganhar: retorno da aposta, mais 100% do seu valor.'
          "\nAs regras do cassino são as seguintes:"
          "\n--> Não aposte o que você não tem em sua carteira. Erros são aceitos,"
          "\nmas se você repeti-los por mais de cinco vezes, os seguranças do cassino"
          "\nte chutam para fora."
          "\n--> Quando você fica zerado, o jogo acaba, e boa sorte da próxima vez!"
          "\nAh, claro, você pode digitar 'fim' a qualquer momento que quiser sair."
          "\n--> Se divirta!")


def define_dificuldade_jogo():
    dificuldade = input("\n\nQual a dificuldade do jogo? (mf, f, m, d): ")
    repostas_possiveis = ["mf", "f", "m", "d"]
    while dificuldade not in repostas_possiveis:
        print("Desculpe, dificuldade não encontrada. Tente de novo.")
        dificuldade = input("\n\nQual a dificuldade do jogo? (mf, f, m, d): ")

    return dificuldade


def define_numero_baralhos(dificuldade_jogo):
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


intro()

dificuldade_jogo = define_dificuldade_jogo()

# Conforme a dificuldade aumenta, a disponibilidade de cartas fica mais escassa.
numero_de_baralhos = define_numero_baralhos(dificuldade_jogo)


# Código para criação de multijogador
lista_jogadores = {}
num_jogadores_string = input('\nQuantos jogadores? ')
num_jogadores = num_jogadores_string
while type(num_jogadores) == type(num_jogadores_string):
    try:
        num_jogadores = int(num_jogadores_string)
        if num_jogadores <= 0 or num_jogadores >= 5:
            print('\nInsira um número inteiro, de 1 a 5')
            num_jogadores_string = input('\nQuantos jogadores? ')
            num_jogadores = num_jogadores_string
    except ValueError:
        print('\nInsira um número inteiro, de 1 a 5')
        num_jogadores_string = input('\nQuantos jogadores? ')

for num in range(num_jogadores):
    nome = input('Nickname do jogador {0}: '.format(num + 1))
    if num == 0:
        lista_jogadores[nome] = 0
    else:
        for jogador in lista_jogadores:
            while nome == jogador:
                print('Nickname indisponível. Insira outro, por favor.')
                nome = input('Nickname do jogador {0}: '.format(num + 1))
        lista_jogadores[nome] = 0

grupo = False
nome_grupo = list(lista_jogadores.keys())[0]
if num_jogadores > 1:
    grupo = True
if grupo:
    nome_grupo = input('Escolham um nome para sua mesa: ')
    while nome_grupo == '':
        nome_grupo = input('Escolham um nome para sua mesa: ')

# Criacao dos baralhos
baralho_base = ["A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥", "A♠", "2♠", "3♠", "4♠",
                "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠", "A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦",
                "9♦", "10♦", "J♦", "Q♦", "K♦", "A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣",
                "K♣"]
valor_cartas = {"A♥": 11, "2♥": 2, "3♥": 3, "4♥": 4, "5♥": 5, "6♥": 6, "7♥": 7, "8♥": 8, "9♥": 9, "10♥": 10, "J♥": 10,
                "Q♥": 10, "K♥": 10, "A♠": 11, "2♠": 2, "3♠": 3, "4♠": 4, "5♠": 5, "6♠": 6, "7♠": 7, "8♠": 8, "9♠": 9,
                "10♠": 10, "J♠": 10, "Q♠": 10, "K♠": 10, "A♦": 11, "2♦": 2, "3♦": 3, "4♦": 4, "5♦": 5, "6♦": 6, "7♦": 7,
                "8♦": 8, "9♦": 9, "10♦": 10, "J♦": 10, "Q♦": 10, "K♦": 10, "A♣": 11, "2♣": 2, "3♣": 3, "4♣": 4, "5♣": 5,
                "6♣": 6, "7♣": 7, "8♣": 8, "9♣": 9, "10♣": 10, "J♣": 10, "Q♣": 10, "K♣": 10}


# Recebe o quanto cada jogador quer colocar na carteira.
for pessoa in lista_jogadores:
    carteira_string = input("{0}, quanto você quer gastar de dinheiro?\n"
                            "(Seu valor de carteira inicial): ".format(pessoa))
    carteira = carteira_string
    while type(carteira) == type(carteira_string):
        try:
            carteira = float(carteira_string)
        except ValueError:
            print('\nTudo bem. Mas agora insira um número, por favor.')
            carteira_string = input(
                "Quanto você quer gastar de dinheiro, {0}? (essa será sua carteira de apostas): ".format(pessoa))
    while carteira <= 0 or carteira > 1000000:
        if carteira <= 0:
            print('\nInsira um valor de dinheiro verdadeiro')
        else:
            print('\nO casino possui um limite de R$1.000.000 por participante')
        carteira_string = input(
            "Quanto você quer gastar de dinheiro, {0}? (essa será sua carteira de apostas): ".format(pessoa))
        carteira = carteira_string
        while type(carteira) == type(carteira_string):
            try:
                carteira = float(carteira_string)
            except ValueError:
                print('\nTudo bem. Mas agora insira um número, por favor.')
                carteira_string = input(
                    "Quanto você quer gastar de dinheiro, {0}? (essa será sua carteira de apostas): ".format(pessoa))
    lista_jogadores[pessoa] = carteira


# Loop do jogo.
# Parametros iniciais, definições de variáveis e listas.
jogador_atual = 0
contador_seguranca = [0] * num_jogadores
expulso = False
existem_jogadores = True

while num_jogadores > 0:
    player = list(lista_jogadores.keys())[jogador_atual]
    aposta_string = input(
        "Quanto você quer apostar nessa rodada, {0}? (Digite 'fim' para sair do jogo): ".format(player))
    if aposta_string == "fim":
        print("\nObrigado por jogar, {0}! Volte sempre!".format(player))
        del lista_jogadores[player]
        del contador_seguranca[jogador_atual]
        num_jogadores -= 1
        aposta_int = aposta_string
        if num_jogadores != 0:
            if jogador_atual == num_jogadores:
                jogador_atual = 0
            player = list(lista_jogadores.keys())[jogador_atual]
        else:
            existem_jogadores = False
        continue
    aposta_int = aposta_string
    while type(aposta_int) == type(aposta_string):
        try:
            aposta_int = float(aposta_string)
        except ValueError:
            aposta_int = 0

    # Criacao do loop para limite de erros na aposta.
    while existem_jogadores and (aposta_int > lista_jogadores[player] or aposta_int <= 0):
        contador_seguranca[jogador_atual] += 1
        if contador_seguranca[jogador_atual] == 5:
            expulso = True
            print("Nós avisamos. Os seguranças cuidarão de você.")
            del lista_jogadores[player]
            del contador_seguranca[jogador_atual]
            num_jogadores -= 1
            if num_jogadores != 0:
                if jogador_atual == num_jogadores:
                    jogador_atual = 0
                player = list(lista_jogadores.keys())[jogador_atual]
            else:
                existem_jogadores = False
            break
        if contador_seguranca[jogador_atual] == 4 and contador_seguranca[jogador_atual] != 5:
            print("\nVocê não pode fazer isso! Aposte de novo. Essa é sua última tentativa\n"
                  "antes de ser expulso da mesa. ")
            aposta_string = input(
                "Quanto você quer apostar nessa rodada? (Digite 'fim' para terminar o jogo): ")
            if aposta_string == "fim":
                print(
                    "\nObrigado por jogar, {0}! Volte sempre!".format(player))
                del lista_jogadores[player]
                del contador_seguranca[jogador_atual]
                num_jogadores -= 1
                aposta_int = aposta_string
                expulso = True
                if num_jogadores != 0:
                    if jogador_atual == num_jogadores:
                        jogador_atual = 0
                    player = list(lista_jogadores.keys())[jogador_atual]
                else:
                    existem_jogadores = False
                break
            aposta_int = aposta_string
            while type(aposta_int) == type(aposta_string):
                try:
                    aposta_int = float(aposta_string)
                except ValueError:
                    aposta_int = 0
            continue
        if contador_seguranca[jogador_atual] < 5:
            print("\nVocê não pode fazer isso! Aposte de novo. Você tem mais {0} tentativas\n"
                  "antes de ser expulso da mesa. ".format(5 - contador_seguranca[jogador_atual]))
            aposta_string = input(
                "Quanto você quer apostar nessa rodada? (Digite 'fim' para terminar o jogo): ")
            if aposta_string == "fim":
                print(
                    "\nObrigado por jogar, {0}! Volte sempre!".format(player))
                del lista_jogadores[player]
                del contador_seguranca[jogador_atual]
                num_jogadores -= 1
                aposta_int = aposta_string
                expulso = True
                if num_jogadores != 0:
                    if jogador_atual == num_jogadores:
                        jogador_atual = 0
                    player = list(lista_jogadores.keys())[jogador_atual]
                else:
                    existem_jogadores = False
                continue
            aposta_int = aposta_string
            while type(aposta_int) == type(aposta_string):
                try:
                    aposta_int = float(aposta_string)
                except ValueError:
                    aposta_int = 0
    if expulso:
        expulso = False
        continue
    if aposta_string == "fim":
        del lista_jogadores[player]
        del contador_seguranca[jogador_atual]
        num_jogadores -= 1
        aposta_int = aposta_string
        if num_jogadores != 0:
            if jogador_atual == num_jogadores:
                jogador_atual = 0
            player = list(lista_jogadores.keys())[jogador_atual]
        else:
            existem_jogadores = False
        continue
    lista_jogadores[player] -= aposta_int

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

    # Computador dá as duas cartas do topo do monte para o jogador
    mao_jogador = monte[0:2].copy()
    del monte[0:2]
    print('\nSuas cartas são {0}.'.format(mao_jogador))
    contador_as = 0
    for carta in mao_jogador:
        if carta == 'A♥' or carta == 'A♠' or carta == 'A♦' or carta == 'A♣':
            contador_as += 1
    valor_mao = valor_cartas[mao_jogador[0]] + valor_cartas[mao_jogador[1]]
    if valor_mao > 21:
        valor_mao -= 10
        contador_as -= 1

    # Checando se há blackjack
    if valor_mao == 21:
        lista_jogadores[player] += 2.5 * aposta_int
        print('BLACKJACK!!!\nVocê ganhou R${0}.\nSaldo atual: {1}.'.format(
            2.5 * aposta_int, lista_jogadores))
        jogador_atual += 1
        if jogador_atual == num_jogadores:
            jogador_atual = 0
        continue

    # Se não há blackjack, jogador escolhe sua ação
    print('Você está com {0} pontos. O que deseja fazer?'.format(valor_mao))
    escolha = input(
        'Digite "mais uma" para mais cartas.\nPressione apenas "Enter" para concluir sua rodada: ')
    while escolha != 'mais uma' and escolha != '':
        print('\nJogada inválida. Agora que começou a rodada, vá até o fim.')
        escolha = input(
            'Digite "mais uma" para mais cartas.\nPressione apenas "Enter" para concluir sua rodada: ')
    indice_carta_mao = 1
    while escolha == 'mais uma':
        indice_carta_mao += 1
        mao_jogador.append(monte[0])
        if monte[0] == 'A♥' or monte[0] == 'A♠' or monte[0] == 'A♦' or monte[0] == 'A♣':
            contador_as += 1
        del monte[0]
        valor_mao += valor_cartas[mao_jogador[indice_carta_mao]]
        if valor_mao == 21:
            break
        if valor_mao > 21:
            if contador_as > 0:
                valor_mao -= 10
                contador_as -= 1
                print('\nSua mão estava estourada, então seu Ás passa a valer 1 ponto.')
            else:
                break
        print('\nSuas cartas são {0}.'.format(mao_jogador))
        print(
            'Você está com {0} pontos. O que deseja fazer?'.format(valor_mao))
        escolha = input('Digite "mais uma" para mais cartas.'
                        '\nPressione apenas "Enter" para concluir sua rodada: ')
        while escolha != 'mais uma' and escolha != '':
            print('Jogada inválida. Agora que começou a rodada, vá até o fim.')
            escolha = input('Digite "mais uma" para mais cartas.'
                            '\nPressione apenas "Enter" para concluir sua rodada: ')

    # Jogo para porque jogador consegue 21
    if valor_mao == 21:
        lista_jogadores[player] += 2.5 * aposta_int
        print('\nSuas cartas são {0}.'.format(mao_jogador))
        print('BLACKJACK!!!'
              '\nVocê ganhou R${0}.'
              '\nSaldo atual: {1}.'.format(2.5 * aposta_int, lista_jogadores))
        jogador_atual += 1
        if jogador_atual == num_jogadores:
            jogador_atual = 0

    # Jogo para porque jogador ultrapassou 21
    elif valor_mao > 21:
        print('\nSuas cartas são {0}.'.format(mao_jogador))
        print('Você está com {0} pontos.'.format(valor_mao))
        print('Você ultrapassou 21 pontos, e perdeu sua aposta.\nSaldo atual: {0}.'.format(
            lista_jogadores))
        if lista_jogadores[player] == 0:
            print('\nSua carteira está vazia.'
                  '\nParece que hoje não era seu dia de sorte...'
                  '\nObrigado por jogar, {0}! Volte sempre!'.format(player))
            del lista_jogadores[player]
            del contador_seguranca[jogador_atual]
            num_jogadores -= 1
            if num_jogadores != 0:
                if jogador_atual == num_jogadores:
                    jogador_atual = 0
                player = list(lista_jogadores.keys())[jogador_atual]
            else:
                existem_jogadores = False
        jogador_atual += 1
        if jogador_atual == num_jogadores:
            jogador_atual = 0

    # Jogador satisfeito com sua mão
    # Aqui inicia o loop da banca
    else:
        cartas_banca = monte[0:2].copy()
        del monte[0:2]
        contador_as = 0
        for carta in cartas_banca:
            if carta == 'A♥' or carta == 'A♠' or carta == 'A♦' or carta == 'A♣':
                contador_as += 1
        valor_banca = valor_cartas[cartas_banca[0]
                                   ] + valor_cartas[cartas_banca[1]]
        if valor_banca > 21:
            valor_banca -= 10
            contador_as -= 1
        # banca para sua jogada com duas cartas
        if not(valor_banca == 21 or valor_banca > valor_mao or (valor_banca >= 17 and valor_banca == valor_mao)
               or (valor_mao > valor_banca >= 17)):
            print('\nSuas cartas: {0}'
                  '\nSeus pontos: {1}'
                  '\nCartas da banca: {2}'
                  '\nPontos da banca: {3}'.format(mao_jogador, valor_mao, cartas_banca, valor_banca))
            input('Pressione "Enter" para continuar.')
        indice_carta_banca = 1
        while valor_banca <= valor_mao and valor_banca < 17:
            indice_carta_banca += 1
            cartas_banca.append(monte[0])
            if monte[0] == 'A♥' or monte[0] == 'A♠' or monte[0] == 'A♦' or monte[0] == 'A♣':
                contador_as += 1
            del monte[0]
            valor_banca += valor_cartas[cartas_banca[indice_carta_banca]]

            # Banca ultrapassou 21 pontos
            if valor_banca > 21:
                if contador_as > 0:
                    valor_banca -= 10
                    contador_as -= 1
                else:
                    break
            elif valor_banca > valor_mao:
                break
            print('\nSuas cartas: {0}'
                  '\nSeus pontos: {1}'
                  '\nCartas da banca: {2}'
                  '\nPontos da banca: {3}'.format(mao_jogador, valor_mao, cartas_banca, valor_banca))
            input('Pressione "Enter" para continuar.')

        # Mensagens finais:
        # Banca ganha com 21
        if valor_banca == 21:
            print('\nÉ Blackjack para a banca... que azar para você.')
            print('\nSuas cartas: {0}'
                  '\nSeus pontos: {1}'
                  '\nCartas da banca: {2}'
                  '\nPontos da banca: {3}'.format(mao_jogador, valor_mao, cartas_banca, valor_banca))
            if valor_banca - valor_mao != 1:
                print('A banca ganhou, por {0} pontos.'
                      '\nSaldo atual: {1}.'.format(valor_banca - valor_mao, lista_jogadores))
            else:
                print('A banca ganhou, por 1 ponto.'
                      '\nSaldo atual: {0}.'.format(lista_jogadores))

        # Banca ultrapassa 21
        elif valor_banca > 21:
            lista_jogadores[player] += 2 * aposta_int
            print('\nSuas cartas: {0}'
                  '\nSeus pontos: {1}'
                  '\nCartas da banca: {2}'
                  '\nPontos da banca: {3}'.format(mao_jogador, valor_mao, cartas_banca, valor_banca))
            print('A banca ultrapassou 21 pontos.'
                  '\nVocê ganhou R${0}!'
                  '\nSaldo atual: {1}.'.format(2 * aposta_int, lista_jogadores))

        # Banca ganha
        elif valor_banca > valor_mao:
            print('\nSuas cartas: {0}'
                  '\nSeus pontos: {1}'
                  '\nCartas da banca: {2}'
                  '\nPontos da banca: {3}'.format(mao_jogador, valor_mao, cartas_banca, valor_banca))
            if valor_banca - valor_mao != 1:
                print('A banca ganhou, por {0} pontos.'
                      '\nSaldo atual: {1}.'.format(valor_banca - valor_mao, lista_jogadores))
            else:
                print('A banca ganhou, por 1 ponto.'
                      '\nSaldo atual: {0}.'.format(lista_jogadores))

        # Jogador ganha
        elif valor_mao > valor_banca:
            lista_jogadores[player] += 2 * aposta_int
            print('\nSuas cartas: {0}'
                  '\nSeus pontos: {1}'
                  '\nCartas da banca: {2}'
                  '\nPontos da banca: {3}'.format(mao_jogador, valor_mao, cartas_banca, valor_banca))
            if valor_mao - valor_banca != 1:
                print('Você ganhou por {0} pontos!'
                      '\nParabéns, você recebeu R${1}!'
                      '\nSaldo atual: {2}'.format(valor_mao - valor_banca, 2 * aposta_int, lista_jogadores))
            else:
                print('Você ganhou por 1 ponto!'
                      '\nParabéns, você recebeu R${0}!'
                      '\nSaldo atual: {1}'.format(2 * aposta_int, lista_jogadores))

        # Empate
        elif valor_banca == valor_mao:
            lista_jogadores[player] += aposta_int
            print('\nSuas cartas: {0}'
                  '\nSeus pontos: {1}'
                  '\nCartas da banca: {2}'
                  '\nPontos da banca: {3}'.format(mao_jogador, valor_mao, cartas_banca, valor_banca))
            print('É um empate! Você recebe sua aposta de volta.'
                  '\nSaldo atual: {0}'.format(lista_jogadores))

        # Verifica se o jogador ainda tem saldo
        if lista_jogadores[player] == 0:
            print(
                '\nSua carteira está vazia.'
                '\nParece que hoje não era seu dia de sorte...'
                '\nObrigado por jogar, {0}! Volte sempre!'.format(player))
            del lista_jogadores[player]
            del contador_seguranca[jogador_atual]
            num_jogadores -= 1
            if num_jogadores != 0:
                if jogador_atual == num_jogadores:
                    jogador_atual = 0
                player = list(lista_jogadores.keys())[jogador_atual]
            else:
                existem_jogadores = False
        else:
            jogador_atual += 1
        if jogador_atual == num_jogadores:
            jogador_atual = 0

if grupo:
    print('Obrigado, {0}, pela sua particpação!'.format(nome_grupo))

# Esta última atualização foi feita na última aula anterior a entrega, com Ana e Rafa trabalhando em conjunto no mesmo computador.
