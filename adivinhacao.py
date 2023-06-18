import random

print('**********************************')
print('Bem vindo ao jogo de adivinhação!')
print('**********************************')

secret_number = random.randrange(0, 101)

total_attempt = 3

for round_game in range(1, total_attempt + 1):
    print('Total de tentativas: {} de {}'.format(round_game, total_attempt))
    attempt = int(input('Digite um número entre 1 e 10: '))

    if attempt < 1 or attempt > 100:
        print('**********************************')
        print("Você digitou: ", attempt)
        print("Você deve digitar um número entre 1 e 10")
        print('**********************************')
        continue
    
    if attempt == secret_number:
        print('**********************************')
        print("Parabens, você acertou!")
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

print('Fim de Jogo')