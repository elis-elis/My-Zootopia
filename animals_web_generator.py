import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')
# print(animals_data)


def print_animals():
    for animal in animals_data:
        print(f'Name:', animal["name"])
        print(f'Diet:', animal["characteristics"]["diet"])
        print(f'Location:', animal["locations"][0])
        if 'type' in animal["characteristics"]:
            print(f'Type:', animal["characteristics"]["type"])
            print()
        else:
            print()
            continue


print_animals()
