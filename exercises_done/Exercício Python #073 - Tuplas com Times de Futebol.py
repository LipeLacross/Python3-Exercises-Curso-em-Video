# Exercício 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol.

teams = (
    'Flamengo', 'Internacional', 'São Paulo', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos',
    'Vasco', 'Corinthians', 'Botafogo', 'Cruzeiro', 'Athletico-PR', 'Bahia', 'Fortaleza', 'Goiás',
    'Ceará', 'Atlético-GO', 'Bragantino', 'São Bento'
)

print("Times do Campeonato Brasileiro:")
for index, team in enumerate(teams, start=1):
    print(f"{index}. {team}")

print(f"\nOs 5 primeiros colocados são: {teams[:5]}")
print(f"Os 4 últimos colocados são: {teams[-4:]}")
print(f"Times em ordem alfabética: {sorted(teams)}")
print(f"O time que está na 5ª posição é {teams[4]}")
