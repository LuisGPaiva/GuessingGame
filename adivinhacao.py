import time #Importa a biblioteca time
import random #Importa a biblioteca random

while True:
# Neste bloco o jogo é apresentado e explicado
        print('Olá! Bem vindo ao jogo de adivinhação!')
        time.sleep(1.5)
        print('Para jogar é muito simples, você deve tentar adivinhar o número de 1 a 10 que eu estou pensando!')
        time.sleep(3)
# No próximo bloco o jogo confirma se o usuário está pronto, gera um número aleatório e recebe o valor digitado pelo usuário
        input('Quando estiver pronto para jogar, clique na tecla [Enter]!')
        n_luck = random.randint (1, 10)
        n_user = input('Digite o seu número: ')
# Neste confere se o valor digitado é um digito (0-9), se True ele continua, se False retorna do início
        if not n_user.isdigit():
            print('Ei! Você deve digitar um NÚMERO INTEIRO DE 1 A 10!')
            time.sleep(2)
            print('Vamos tentar novamente...')
            time.sleep(2)
            continue

        n_user = int(n_user) # Transforma o digito recebido do usuário em um Número inteiro(int)

        if n_user < 1 or n_user > 10: # Confere se o número digitado está entra 1 e 10, se não estiver, volta do começo
            print('Ei! Você deve digitar um NÚMERO INTEIRO DE 1 A 10!')
            time.sleep(2)
            print('Vamos tentar novamente...')
            time.sleep(2)
            continue
        if n_luck == n_user: # Confere a condição de vitória do usuário, se True, finaliza o script
            print('Parabéns, você acertou o número que eu estava pensando!')
            print('E com isso você ganhou...')
            time.sleep(2)
            print('...')
            time.sleep(2)
            print('NADA!')
            break
        else: # Confere a condição de derrota do usuário, se True, oferece a opção de reiniciar o script apertando Enter
            print('Que pena, você não acertou! :{')
            print('O número que eu estava pensando era o', n_luck, '!')
            time.sleep(2)
            input('Caso queira jogar novamente é só clicar na tecla [Enter]!')
            time.sleep(1)