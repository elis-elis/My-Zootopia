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


def generate_animals_info():
    """Generates a string with the HTML content for the animals' data."""
    output = ''
    for animal in animals_data:
        # append information to each string
        output += '<li class="cards__item">'
        output += f'<div class="card__title"> {animal["name"]}<br/></div>\n'
        output += '<p class="card__text">'
        output += f'<strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'
        output += f'<strong>Location:</strong> {animal["locations"][0]}<br/>\n'
        if 'type' in animal["characteristics"]:
            output += f'<strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'
        output += '</p>'
        output += '</li>'
    print(output)
    return output


# generate_animals_info()


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
    animal_info = generate_animals_info()
    replaced_template = replace_placeholder(template_content, animal_info)
    write_to_html_file(replaced_template)


if __name__ == "__main__":
    main()

