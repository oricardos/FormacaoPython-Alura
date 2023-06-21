import random


def guessing_game():
    print('**********************************')
    print('Bem vindo ao jogo de adivinhação!')
    print('**********************************')

    secret_number = random.randrange(0, 101)
    total_attempt = 0
    points = 1000

    print('Escolha o nível do Jogo', secret_number)
    print('(1) Fácil (2) Médio (3) Difícil')

    level = int(input('Selecione um nível: '))

    if level == 1:
        total_attempt = 20
    elif level == 2:
        total_attempt = 10
    else:
        total_attempt = 5

    for round_game in range(1, total_attempt + 1):
        print('Total de tentativas: {} de {}'.format(round_game, total_attempt))
        attempt = int(input('Digite um número entre 1 e 100: '))

        if attempt < 1 or attempt > 100:
            print('**********************************')
            print("Você digitou: ", attempt)
            print("Você deve digitar um número entre 1 e 100")
            print('**********************************')
            continue

        if attempt == secret_number:
            print('**********************************')
            print("Parabens, você acertou! Seus pontos foram: {}".format(points))
            print('**********************************')
            break
        else:
            if attempt > secret_number:
                print('**********************************')
                print("Você digitou: ", attempt)
                print('O número secreto é menor do que o número que você tentou')
                print('**********************************')
            elif attempt < secret_number:
                print('**********************************')
                print("Você digitou: ", attempt)
                print('O número secreto é maior do que o número que você tentou')
                print('**********************************')

            lost_points = abs(secret_number - attempt)
            points = points - lost_points

    print('Fim de Jogo')


if __name__ == '__main__':
    guessing_game()
