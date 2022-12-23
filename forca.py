from random import randint

corpo = [
'''
    +#####+
    |     |
          |
          |
          |
          |
          |
          |
###########''',
'''
    +#####+  
    |     |
    0     |
          |
          |
          |
          |
          |
###########''',
'''
    +#####+
    |     |
    0     |
    |     |
          |
          |
          |
          |
###########''',
'''
    +#####+
    |     |
    0     |
   /|     |
          |
          |
          |
          |
###########''',
'''
    +#####+
    |     |
    0     |
   /|\    |
          |
          |
          |
          |
###########''',
'''
    +#####+
    |     |
    0     |
   /|\    |
   /      |
          |
          |
          |
###########''',
'''
    +#####+
    |     |
    0     |
   /|\    |
   / \    |
          |
          |
          |
###########''',
]

palavras = ['amarelo', 'amiga', 'amor', 'ave', 'contexto', 'esquerdo', 'Bola', 'impacto', 'bolo', 'branco', 'cama',
'caneca', 'caminho', 'clube', 'copo', 'doce', 'elefante', 'escola', 'estojo', 'faca', 'foto', 'garfo', 'geleia',
'girafa', 'janela', 'limonada', 'coelho', 'meia', 'noite', 'chuveiro', 'universidade', 'ovo', 'pai', 'basquete',
'parque', 'passarinho', 'peixe', 'pijama', 'rato', 'umbigo']

def get_palavra(p_lista):
    '''
    Função que retorna uma palavra da lista "palavras"
    :param palavra:
    :return 1 palavra:
    '''
    p_index = randint(0, len(p_lista)-1)
    return p_lista[p_index]

def display(corpo, letra_errada, letra_correta, palavra_secreta):
    print(corpo[len(letra_errada)])
    print()

    print('Letras erradas: ', end=' ')

    for letra in letra_errada:
        print(letra, end=' ')
    print()

    lacuna = '_' * len(palavra_secreta)

    # Substituindo os espaços em branco pelas letras corretas
    for cont in range(len(palavra_secreta)):
        if palavra_secreta[cont] in letra_correta:
            lacuna = lacuna[:cont] + palavra_secreta[cont] + lacuna[cont+1:]

    # Mostrar a palavra secreta com espaços entre cada letra
    for letra in lacuna:
        print(letra, end=' ')
    print()

def get_chute(letra_chutada):
    '''
    Garante que o usuário insira apenas uma letra
    :param letra_chutada:
    :return letra escolhida pelo usuário:
    '''

    while True:
        chute = str(input('Letra: ')).lower().strip()

        if len(chute) != 1:
            print('\033[7;31mPor favor, digite apenas uma letra!\033[m')
        elif chute in letra_chutada:
            print('\033[7;32mAhh, essa você já chutou! Tente outra...\033[m')
        elif chute not in 'abcdefghijklmnopqrstuvwxyz':
            print('\033[7;31mPor favor, digite uma letra\033[m')
        else:
            return chute

def jogar_novamente():
    '''
    Retornar True caso o usuário queira jogar novamente
    :return:
    '''

    return input('Deseja jogar novamente? [S] para sim ou [N] para não: ').lower().startswith('s')

print('### C A R R A S C O ###')
letra_errada = ''
letra_correta = ''
palavra_secreta = get_palavra(palavras)
fim_de_jogo = False

while True:
    display(corpo, letra_errada, letra_correta, palavra_secreta)

    chute = get_chute(letra_errada + letra_correta)

    if chute in palavra_secreta:
        letra_correta = letra_correta + chute
        p_completa = True

        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] not in letra_correta:
                p_completa = False
                break

        if p_completa:
            print(f'\nParabéns, você acertou!! A palavra secreta é: {palavra_secreta}')
            print("       ___________      ")
            print("      '._==_==_=_.'     ")
            print("      .-\\:      /-.    ")
            print("     | (|:.     |) |    ")
            print("      '-|:.     |-'     ")
            print("        \\::.    /      ")
            print("         '::. .'        ")
            print("           ) (          ")
            print("         _.' '._        ")
            print("        '-------'       ")
            fim_de_jogo = True

    else:
        letra_errada = letra_errada + chute

        if len(letra_errada) == len(corpo) - 1:
            display(corpo, letra_errada, letra_correta, palavra_secreta)

            print(f'Que pena, suas chanes acabaram... \nTotal de chutes errados: {len(letra_errada)}\n'
                  f'Total de chutes corretos: {len(letra_correta)}\nAhh, a palavra era: {palavra_secreta}')
            print("    _______________         ")
            print("   /               \       ")
            print("  /                 \      ")
            print("//                   \/\  ")
            print("\|   XXXX     XXXX   | /   ")
            print(" |   XXXX     XXXX   |/     ")
            print(" |   XXX       XXX   |      ")
            print(" |                   |      ")
            print(" \__      XXX      __/     ")
            print("   |\     XXX     /|       ")
            print("   | |           | |        ")
            print("   | I I I I I I I |        ")
            print("   |  I I I I I I  |        ")
            print("   \_             _/       ")
            print("     \_         _/         ")
            print("       \_______/           ")
            fim_de_jogo = True

    # Verificar se o jogador deseja jogar novamente
    if fim_de_jogo:
        if jogar_novamente():
            letra_errada = ''
            letra_correta = ''
            fim_de_jogo = False
            palavra_secreta = get_palavra(palavras)
        else:
            break
 
