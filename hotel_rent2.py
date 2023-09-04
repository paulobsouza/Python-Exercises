# Crie um sistema para reservas de quartos de hotel, com funcionalidades para verificar disponibilidade, fazer reservas e cancelar reservas.
# Use classes para representar quartos, clientes e o sistema de reservas.

class Hotel:
    def __init__(self):
        self.rooms = []
        self.clients = []

    def get_room_by_code(self, code):
        for room in self.rooms:
            if room.code_room == code:
                return room
        return None

    def check_availability(self, code):
        room = self.get_room_by_code(code)
        if room:
            return room.availability
        return None


    def make_reservation(self, code=None, client_name=None):
        if not client_name:
            return 'Nome do cliente não fornecido.'

        available_rooms = [room for room in self.rooms if room.availability]

        if not available_rooms:
            return 'Não há quartos disponíveis para reserva.'

        if code:
            room = self.get_room_by_code(code)
            if room and room.availability:
                room.availability = False
                room.client_name = client_name
                self.clients.append(Client(client_name, room))
                return f'Reserva efetuada para o quarto de número {room.code_room}.', room
            return 'Quarto não disponível para reserva com o código fornecido.'
        else:
            room = available_rooms[0]
            room.availability = False
            room.client_name = client_name
            self.clients.append(Client(client_name, room))
            return f'Reserva efetuada para o quarto de número {room.code_room}.'


    def cancel_reservation(self, code, client_name):
        room = self.get_room_by_code(code)
        if room:
            client_to_remove = None
            for client in self.clients:
                if client.name == client_name and client.room == room:
                    client_to_remove = client
                    break
            if client_to_remove:
                self.clients.remove(client_to_remove)
                room.availability = True
                return f'Reserva do quarto de número {room.code_room} cancelada.'
            return 'Nenhum cliente encontrado para este quarto.'
        return 'Quarto não encontrado.'


class Room:
    def __init__(self, code):
        self.code_room = code
        self.availability = True
        self.client_name = None


class Client:
    def __init__(self, name, room):
        self.name = name
        self.room = room


hotel = Hotel()

while True:
    log = int(input('Para acessar a área de clientes digite 1, para a área de funcionários digite 2. '))
    
    if log == 2:
        while True:
            action_h = int(input('Para ver o quadro de reservas digite 1, para adicionar uma reserva digite 2, para remover uma reserva digite 3, para adicionar um quarto digite 4, para remover um quarto digite 5, para sair digite 6. '))
            for room in hotel.rooms:
                if action_h == 1:
                    print(f'Quarto {room.code_room}: {"Disponível" if room.availability else f"Ocupado pelo cliente {room.client_name}"}')
                elif action_h == 2:
                    print(f'Quarto {room.code_room}: {"Disponível" if room.availability else f"Ocupado pelo cliente {room.client_name}"}')
                    code = input('Qual a identificação do quarto? ')
                    client_name = input('Qual o nome do cliente? ')
                    result = hotel.make_reservation(code, client_name)
                    print(result)
                elif action_h == 3:
                    print(f'Quarto {room.code_room}: {"Disponível" if room.availability else f"Ocupado pelo cliente {room.client_name}"}')
                    code = input('Qual a identificação do quarto? ')
                    client_name = input('Qual o nome do cliente? ')
                    result = hotel.cancel_reservation(code, client_name)
                    print(result)
                elif action_h == 4:
                    add = input('Qual a identificação do quarto a ser adicionado? ')
                    room = Room(add)
                    hotel.rooms.append(room)
                    print(f'Quarto {add} adicionado com sucesso.')
                    print(f'Quarto {room.code_room}: {"Disponível" if room.availability else f"Ocupado pelo cliente {room.client_name}"}')
                elif action_h == 5:
                    print(f'Quarto {room.code_room}: {"Disponível" if room.availability else f"Ocupado pelo cliente {room.client_name}"}')
                    rem = input('Qual a identificação do quarto que deve ser removido? ')
                    room_to_remove = hotel.get_room_by_code(rem)
                    if room_to_remove:
                        if room_to_remove.availability:
                            hotel.rooms.remove(room_to_remove)
                            print(f'Quarto {rem} removido com sucesso.')
                            print(f'Quarto {room.code_room}: {"Disponível" if room.availability else f"Ocupado pelo cliente {room.client_name}"}')
                    else:
                        print(f'O quarto {rem} não pode ser removido porque está ocupado.')
                        print(f'Quarto {room.code_room}: {"Disponível" if room.availability else f"Ocupado pelo cliente {room.client_name}"}')
                        print(f'Quarto {rem} não encontrado.')
                elif action_h == 6:
                    break

    elif log == 1:
        action_c = int(input('Para fazer uma reserva digite 1, para cancelar uma reserva digite 2. '))
        if action_c == 1:
            room = hotel.rooms
            if room in hotel.rooms: 
                print(f'Quarto {room.code_room}: {"Disponível" if room.availability else f"Ocupado"}')
                client_name = input('Qual o seu nome? ')
            else: 
                print('Não há quartos disponiveís no momento.')
            for room in hotel.rooms:
                if room.availability:
                    hotel.make_reservation(0, client_name)
                    print('Reserva feita com sucesso.')
                else:
                    print(f'Quarto {room.code_room}: Ocupado')
        elif action_c == 2:
            client_name = input('Qual o seu nome? ')
            hotel.cancel_reservation(0, client_name) 
            print('Reserva cancelada.')
        else:
            print('Há um erro. Por favor, verifique.')

    else:
        print('Opção inválida.')
