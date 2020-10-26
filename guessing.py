from random import randint


def play():
    print('*****************************')
    print('Bem vindo ao primeiro projeto')
    print('*****************************')

    secret_number = randint(1, 50)
    try_number = 0
    points = 1000

    print('Escolha o nível de dificuldade')
    print('[1] fácil, [2] Médio [3] Difícil')

    level = int(input('Escolha o nível: '))

    if level == 1:
        try_number = 10
    elif level == 2:
        try_number = 6
    elif level == 3:
        try_number = 3

    for start in range(1, try_number + 1):
        print(f'Tentativa: {start} de {try_number}')

        user_number = int(input('Digite um número entre 1 e 50: '))

        major = secret_number > user_number
        minor = secret_number < user_number

        if user_number == secret_number:
            print(f'Você acertou e fez {points} pontos')
            break
        else:
            if major:
                print('O número secreto é maior que o digitado')
            elif minor:
                print('O número secreto é menor que o digitado')

                lost_points = abs(secret_number - try_number)
                points = points - lost_points

    print(f'Sua pontuação é {points}')


# preenche a variável __name__ quando o arquivo é chamado direto
if __name__ == '__main__':
    play()
