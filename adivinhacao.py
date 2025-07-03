import time
import random

while True:

        print('Olá! Bem vindo ao jogo de adivinhação!')
        time.sleep(1.5)
        print('Para jogar é muito simples, você deve tentar adivinhar o número de 1 a 10 que eu estou pensando!')
        time.sleep(3)

        input('Quando estiver pronto para jogar, clique na tecla [Enter]!')
        n_luck = random.randint (1, 10)
        n_user = input('Digite o seu número: ')

        if not n_user.isdigit():
            print('Ei! Você deve digitar um NÚMERO INTEIRO DE 1 A 10!')
            time.sleep(2)
            print('Vamos tentar novamente...')
            time.sleep(2)
            continue

        n_user = int(n_user)

        if n_user < 1 or n_user > 10:
            print('Ei! Você deve digitar um NÚMERO INTEIRO DE 1 A 10!')
            time.sleep(2)
            print('Vamos tentar novamente...')
            time.sleep(2)
            continue
        if n_luck == n_user:
            print('Parabéns, você acertou o número que eu estava pensando!')
            print('E com isso você ganhou...')
            time.sleep(2)
            print('...')
            time.sleep(2)
            print('NADA!')
            break
        else:
            print('Que pena, você não acertou! :{')
            print('O número que eu estava pensando era o', n_luck, '!')
            time.sleep(2)
            new_game = input('Caso queira jogar novamente é só clicar na tecla [Enter]!')
            time.sleep(1)