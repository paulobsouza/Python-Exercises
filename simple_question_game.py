questions = [
    {
        'Question': 'How much is 2 + 2?',
        'Options': ['1', '3', '4', '5'],
        'Answer': '4',
    },
    {
        'Question': 'How much is 5 x 5?',
        'Options': ['25', '55', '10', '51'],
        'Answer': '25',
    },
    {
        'Question': 'How much is 10 / 2?',
        'Options': ['4', '5', '2', '1'],
        'Answer': '5',
    },
]

for question in questions:
    print('Question:', question['Question'])
    print()

    for i, option in enumerate(question['Options']):
        f'{i})', option
    print()

    choice = input('Choice an option: ')
    hit = False
    int_choice = None

    if choice.isdigit():
        int_choice = int(choice)

    if int_choice is not None:
        if int_choice == question['Answer']:
            hit = True

    if hit:
        print('Você está certo!')
    else:
        print('Você está errado.')
print()
