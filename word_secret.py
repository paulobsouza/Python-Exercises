import os  # import model os for access the os functions

secret_word = 'Ornitorrinco'
letter_hits = ''
user_attempts = 0

while True:
    letter = input('Digite uma letra: ')
    user_attempts += 1

    if len(letter) > 1:  # restricting the user
        print('Digite apenas uma letra')
        continue

    if letter in secret_word:
        letter_hits += letter

    word_user = ''

    for secret_letter in secret_word:
        if secret_letter in letter_hits:
            word_user += secret_letter
        else:
            word_user += '*'
    print(word_user)

    if word_user == secret_word:
        os.system('clear')  # for clear the terminal

        print('Você acertou a palavra secreta! Parabéns!')
        f'A palavra secreta era {"secret_word"}'
        f'O número de tentativas foi de: {user_attempts}x'

        letter_hits = ''
        user_attempts = 0
