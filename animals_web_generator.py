import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')


def read_template():
    """Reads the HTML template file and returns its content as a string."""
    with open('animals_template.html', 'r') as content:
        return content.read()


def serialize_animal(animal_obj):
    """Generates a string with the HTML content for a single animal."""
    output = ''
    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal_obj["name"]}</div>\n'
    output += '<p class="card__text">\n'
    output += f'<strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n'
    output += f'<strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'
    if 'type' in animal_obj["characteristics"]:
        output += f'<strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n'
    output += '</p>\n'
    output += '</li>\n'
    return output


def generate_animals_info(data):
    """Generates a string with the HTML content for all animals."""
    output = ''
    for animal in data:
        output += serialize_animal(animal)
    return output


def replace_placeholder(template, replacement):
    """Replaces the placeholder text in the HTML template
    with the provided replacement string.
    """
    return template.replace("__REPLACE_ANIMALS_INFO__", replacement)


def write_to_html_file(content):
    """Writes the provided HTML content to a new file."""
    with open('animals.html', "w") as new_file:
        return new_file.write(content)


def main():
    template_content = read_template()
    animal_info = generate_animals_info(animals_data)
    replaced_template = replace_placeholder(template_content, animal_info)
    write_to_html_file(replaced_template)


if __name__ == "__main__":
    main()
