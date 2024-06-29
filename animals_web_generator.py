import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')


# print(animals_data)


def print_animals():
    """ Prints information about animals from a provided JSON data structure.

        This function iterates over a list of animal dictionaries (loaded
        presumably from a JSON file) and prints details about each animal,
        including its name, diet, location, and type (if available).

        Args:
            No parameter (data is loaded from 'animals_data')

        Returns:
            None
    """
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
