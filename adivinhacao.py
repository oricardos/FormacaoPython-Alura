print('**********************************')
print('Bem vindo ao jogo de adivinhação!')
print('**********************************')

secret_number = 10

attempt = int(input('Digite um número entre 1 e 10: '))

if attempt > 10:
    print('Só até 10 doido')
elif attempt != secret_number:
    print('Tente novamente!')
else:
    print('Acertou, miserável')

print('Fim de Jogo')