import os

array = []
while True:
    print('Selecione uma opção. ')
    options = input('[i]nserir, [d]eletar, [l]istar ou [s]air ')

    if options == 'i':
        os.system('clear')
        insert = input('O que deseja inserir? ')
        array.append(insert)
        f'{insert} foi inserido a lista.'

    elif options == 'd':
        os.system('clear')
        delete_str = input('O que deseja apagar? ')

        try:
            i = int(delete_str)
            del array[i]
            f'{i} foi removido da lista.'

        except ValueError:
            f'{delete_str} não é um valor inteiro, por favor digite o índice do item desejado.'
        except IndexError:
            f'{delete_str} não está na lista.'
        except Exception:
            print('Erro desconhecido.')

    elif options == 'l':
        os.system('clear')
        
        if len(array) == 0:
            print('Não há nada na lista.')
        
        for i, value in enumerate(array):
            print(i, value) 

    elif options == 's':
        break

    else:
        print('Nenhuma operação existente foi selecionada. Por favor, escolha "i", "d" ou "l". ')
    
