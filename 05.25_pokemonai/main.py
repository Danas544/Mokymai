from typing import Dict, Optional
import random
import requests
from pokemon import Pokemon, Statistic
# pylint: disable-all

POKEMON_ENDPOINT = "https://pokeapi.co/api/v2/pokemon/"


def get_random_pokemon() -> Dict[str, str]:
    pokemon_id = random.randint(1, 1010)
    pokemon = requests.get(f"{POKEMON_ENDPOINT}{pokemon_id}")
    return pokemon.json()

def convert_json_to_pokemon(api_response: Dict[str, str]) -> Pokemon:
    name = api_response["name"]
    response_stats = api_response["stats"]
    stats = []
    for response_stat in response_stats:
        stats.append(Statistic(response_stat["base_stat"],
                               response_stat["stat"]["name"]))
    return Pokemon(name, stats)

def get_all_stats_name() -> list[str]:
    stats_name = []
    stats = requests.get(f'https://pokeapi.co/api/v2/stat/')
    stats_json = stats.json()
    for x in stats_json['results']:
        stats_name.append(x['name'])
    return stats_name




def choose_winner(pokemon1: Pokemon, pokemon2: Pokemon) -> Optional[Pokemon]:
    all_stats = get_all_stats_name()
    p1_score = 0
    p2_score = 0
    for statistic in all_stats:
        p1_stat_points = pokemon1.get_statistic_base_stat(statistic)
        p2_stat_points = pokemon2.get_statistic_base_stat(statistic)
        if p1_stat_points > p2_stat_points:
            p1_score += 1
        elif p2_stat_points > p1_stat_points:
            p2_score += 1
    if p1_score > p2_score:
        return pokemon1
    elif p1_score < p2_score:
        return pokemon2
    else:
        return None


if __name__ == "__main__":

    pokomen1 = convert_json_to_pokemon(get_random_pokemon())
    pokomen2 = convert_json_to_pokemon(get_random_pokemon())

    winner = choose_winner(pokomen1, pokomen2)

    print(f"first pokomen: {pokomen1}")
    print(f"second pokomen: {pokomen2.name}")

    if winner:
        print(f'winner: {winner.name}')
    else:
        print('draw')