print('**********************************')
print('Bem vindo ao jogo de adivinhação!')
print('**********************************')

secret_number = 10



total_attempt = 3

for round_game in range(1, total_attempt + 11):
    print('Total de tentativas: {} de {}'.format(round_game, total_attempt))
    attempt = int(input('Digite um número entre 1 e 10: '))
    
    if attempt == secret_number:
        print('acertou')
    else:
        if attempt > secret_number:
            print('número maior')
        elif attempt < secret_number:
            print('número menor')

print('Fim de Jogo')