import requests


def fetch_animal(name):
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': 'a0ZGEN85wwKRoRX/pNb9eQ==QwE9jROfxws2oVNM'})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)


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
    animal_name = input("Enter animal you want to know: ")
    animals_data = fetch_animal(animal_name)
    if animals_data:
        template_content = read_template()
        animal_info = generate_animals_info(animals_data)
        replaced_template = replace_placeholder(template_content, animal_info)
        write_to_html_file(replaced_template)
    print("it's all done. Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
