"""
Faça um programa que a partir da lista de times com as informações de gols e derrotas
Imprima o time com maior/menor quantidade de gols e maior/menor quantidade de derrotas.
"""

times = [
    {"time": "A", "gols": 1, 'derrotas':4},
    {"time": "B", "gols": 4, 'derrotas': 11},
    {"time": "C", "gols": 31, 'derrotas': 13},
    {"time": "D", "gols": 50, 'derrotas': 5}
]

max_gols = 0
max_derrotas = 0
for time in times:
    if max_gols < time['gols']:
        max_gols = time['gols']
        time_max_gols = time['time']

    if max_derrotas < time['derrotas']:
        max_derrotas = time['derrotas']
        time_max_derrotas = time['time']

min_gols = max_gols
min_derrotas = max_derrotas

for time in times:
    if min_gols > time['gols']:
        min_gols = time['gols']
        time_min_gols = time['time']

    if min_derrotas > time['derrotas']:
        min_derrotas = time['derrotas']
        time_min_derrotas = time['time']

print("""Máximo de Gols ==> Time: {} Gols: {}
Mínimo de Gols ==> Time: {} Gols: {}""".format(time_max_gols,max_gols,time_min_gols,min_gols,))

print("""\nMáximo de derrotas ==> Time: {} derrotas: {}
Mínimo de derrotas ==> Time: {} derrotas: {}""".format(time_max_derrotas,max_derrotas,time_min_derrotas,min_derrotas))
