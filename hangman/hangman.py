import random


def play():
    welcome()
    secret_word = get_secret_word()

    correct_letters = show_correct_letters(secret_word)
    print(correct_letters)

    hanged = False
    matched = False
    errors = 0

    while(not hanged and not matched):
        try_letter = player_try_letter()

        if try_letter in secret_word:
            correct_try_letter(secret_word, try_letter, correct_letters)

        else:
            errors += 1
            print_hangman(errors)

        hanged = errors == 7
        matched = "_" not in correct_letters
        print(correct_letters)

    if matched:
        win_message()
    else:
        lose_message(secret_word)


def welcome():
    print('*****************************')
    print('Bem vindo ao jogo de Forca')
    print('*****************************')


def get_secret_word():
    words = []

    with open('hangman/words.txt', 'r') as file:
        for line in file:
            line = line.strip()
            words.append(line)

    file.close()

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word


def show_correct_letters(secret_word):
    correct_letters = ['_' for letter in secret_word]
    return correct_letters


def player_try_letter():
    try_letter = input('Qual Letra?')
    try_letter = try_letter.strip().upper()
    return try_letter


def correct_try_letter(secret_word, try_letter, correct_letters):
    index = 0

    for letter in secret_word:
        if(try_letter == letter):
            correct_letters[index] = letter
        index += 1


def win_message():
    print("Parabéns, você ganhou!")
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


def lose_message(secret_word):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {secret_word}")
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


def print_hangman(errors):
    print(f'Essa letra não existe, você ainda tem {7 - errors} tentativas')
    print("  _______     ")
    print(" |/      |    ")

    if(errors == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(errors == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(errors == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(errors == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(errors == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(errors == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errors == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


# preenche a variável __name__ quando o arquivo é chamado direto
if __name__ == '__main__':
    play()
