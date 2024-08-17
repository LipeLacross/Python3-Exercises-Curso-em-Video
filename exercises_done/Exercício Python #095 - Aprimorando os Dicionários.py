# Exercício 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

players = []

while True:
    player = {}
    player['name'] = input("Nome do jogador: ")
    num_matches = int(input("Quantas partidas ele jogou? "))
    player['goals'] = [int(input(f"Quantos gols na partida {i+1}? ")) for i in range(num_matches)]
    player['total_goals'] = sum(player['goals'])
    players.append(player)

    continue_input = input("Quer continuar? (S/N): ").upper()
    if continue_input == 'N':
        break

while True:
    query = input("Mostrar dados de qual jogador? (Digite 'Sair' para encerrar): ")
    if query == 'Sair':
        break

    for player in players:
        if player['name'] == query:
            print(f"\n{player['name']} jogou {len(player['goals'])} partidas e fez {player['total_goals']} gols.")
            for i, goals in enumerate(player['goals']):
                print(f"Na partida {i+1} fez {goals} gols.")
            break
    else:
        print("Jogador não encontrado.")
