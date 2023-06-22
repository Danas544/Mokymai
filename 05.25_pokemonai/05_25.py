import requests


# stats = []

# def get_stats_name(page):
#     stats = requests.get(f'https://pokeapi.co/api/v2/stat/{page}')
#     stats_json = stats.json()
#     return stats_json['name']

# x = 1
# for page in range(1,9):
#     stats.append(get_stats_name(x))
#     x += 1

# print (stats)


def get_all_stats_name() -> list[str]:
    stats_name = []
    stats = requests.get(f'https://pokeapi.co/api/v2/stat/')
    stats_json = stats.json()
    for x in stats_json['results']:
        stats_name.append(x['name'])
    return stats_name


x = get_all_stats_name()
print(x)
