# Crie uma classe para representar um jogador de futebol, com os atributos nome, posição, data de nascimento, nacionalidade, altura e peso. 
# Crie os métodos públicos necessários para sets e gets e também um método para imprimir todos os dados do jogador. 
# Crie um método para calcular a idade do jogador e outro para mostrar quanto tempo falta para o jogador aposentar.
# Considere que os jogadores da defesa se aposentam aos 40 anos, os jogadores de meio-campo aos 38 e os atacantes aos 35.

YEAR = 2023

class FootballPlayer:
   def __init__(self, name):
     self._name = name
     self._position = ''
     self._nationality = ''
     self._birth_date = 0
     self._height = 0
     self._weight = 0
            
   @property
   def position(self):
     return self._position
            
   @position.setter
   def position(self, position):
     self._position = position
            
   @property
   def nationality(self):
        return self._nationality
       
   @nationality.setter
   def nationality(self, nationality):
        self._nationality = nationality   
           
   @property
   def birth_date(self):
        return self._birth_date
       
   @birth_date.setter
   def birth_date(self, birth_date):
        self._birth_date = birth_date
       
   @property
   def height(self):
       return self._height
       
   @height.setter
   def height(self, height):
       self._height = height
           
   @property
   def weight(self):
       return self._weight
           
   @weight.setter
   def weight(self, weight):
       self._weight = weight
            
   def data_player(self):
       return print([self._name, self._position, self._nationality, self._birth_date, self._height, self._weight])
        
   def age(self, birth_date):
       return(YEAR - birth_date)
        
   def retiree(self, birth_date, position):
       _age = self.age(birth_date)
       position = position
       if (_age >= 40) and (position == 'defensor'):
         return ('O jogador está aposentado.')
       elif (_age <= 40) and (position == 'defensor'):
         return f'Faltam {40 - _age} anos para o jogador se aposentar'
       elif (_age >= 38) and (position == 'meio-campista'):
         return ('O jogador está aposentado.')
       elif (_age <= 38) and (position == 'meio-campista'):
         return f'Faltam {38 - _age} anos para o jogador se aposentar'
       elif (_age >= 35) and (position == 'atacante'):
         return ('O jogador está aposentado.')
       elif (_age <= 35) and (position == 'atacante'):
         return f'Faltam {35 - _age} anos para o jogador se aposentar'
       else:
         return "Há erro em alguma das informações."
     
        
name = input('Digite o nome do jogador: ')
player = FootballPlayer(name.upper())
print('Informe os dados básicos: ')
p = input('Qual a posição do jogador? (Defensor / Meio-campista / Atacante) ').lower()
player.position = p.upper()
n = input('Qual a nacionalidade do jogador? ')
player.nationality = n.upper()
b = int(input('Quando nasceu o jogador? '))
player.birth_date = b
h = input('Qual a altura do jogador? ')
player.height = h
w = input('Qual o peso do jogador? ')
player.weight = w

player.data_player()
print(player.retiree(b, p))
