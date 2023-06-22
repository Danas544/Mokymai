import unittest, mock

from main import get_random_pokemon, convert_json_to_pokemon , get_all_stats_name

# pylint: disable-all



# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'https://pokeapi.co/api/v2/stat/':
        return MockResponse(
            {
   "results":[
      { "name":"hp"},
      {"name":"attack"},
      {"name":"defense"},
      { "name":"special-attack"},
      {"name":"special-defense"},
      {"name":"speed"},
      {"name":"accuracy"},
      {"name":"evasion"},

   ]
}, 200
        )


    return MockResponse(None, 404)

def mocked_requests_get2(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data
        
    if args[0] == f'https://pokeapi.co/api/v2/pokemon/1':
        return MockResponse(
            {
   "name": "bulbasaur",
   "stats":[{"base_stat":45,"stat":{"name":"hp"}},
            {"base_stat":49,"stat":{"name":"attack"}},
            {"base_stat":49,"stat":{"name":"defense"}},
            {"base_stat":65, "stat":{"name":"special-attack"}},
            {"base_stat":65,"stat":{"name":"special-defense"}},
            {"base_stat":45, "stat":{"name":"speed"}}]

            }, 200
        )


class TestIntegration(unittest.TestCase):

    @mock.patch('requests.get', side_effect= mocked_requests_get2)
    @mock.patch('random.randint', side_effect= "1")
    def test_geting_pokemon_and_converting_json(self, *args):
        api_response = get_random_pokemon()
        pokemon = convert_json_to_pokemon(api_response)
        self.assertEqual(pokemon.name,'bulbasaur')
        self.assertEqual(pokemon.stats,"Statistic(base_stat=45, name='hp'), Statistic(base_stat=49, name='attack'), Statistic(base_stat=49, name='defense'), Statistic(base_stat=65, name='special-attack'), Statistic(base_stat=65, name='special-defense'), Statistic(base_stat=45, name='speed')")

    @mock.patch('requests.get', side_effect= mocked_requests_get)
    def test_geting_all_stat_names(self, mock_requests):
        stat_names = get_all_stats_name()
        self.assertEqual(stat_names, ['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed', 'accuracy', 'evasion'])

