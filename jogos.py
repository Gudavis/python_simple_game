import forca
import adivinhacao


def choose_game():
    print('*****************************')
    print('Escolha o seu jogo')
    print('*****************************')

    print('(1)Adivinhação (2) Forca')

    game = int(input('Qual Jogo você quer? '))

    if game == 1:
        print('Jogando Adivinhação')
        adivinhacao.play()
    elif game == 2:
        print('Jogando Forca')
        forca.play()


if __name__ == '__main__':
    choose_game()
