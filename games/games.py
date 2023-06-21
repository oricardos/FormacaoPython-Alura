import hangman_game
import guessing_game

print('**************************************')
print('*** Escolha qual jogo deseja jogar ***')
print('**************************************')

print('(1) - Forca | (2) - Adivinhação')

game = int(input('Qual jogo  vai ser hoje?'))

if game == 1:
    print('*** Forca selecionado ***')
    hangman_game.hangman_game()
else:
    print('*** Adivinhação Selecionado ***')
    guessing_game.guessing_game()
