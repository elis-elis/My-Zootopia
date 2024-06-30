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
        output += f'Name: {animal["name"]}\n'
        output += f'Diet: {animal["characteristics"]["diet"]}\n'
        output += f'Location: {animal["locations"][0]}\n'
        if 'type' in animal["characteristics"]:
            output += f'Type: {animal["characteristics"]["type"]}\n'
    return output


# generate_animals_info()


def replace_placeholder(template, replacement):
    """Replaces the placeholder text in the HTML template with the provided replacement string.

    Args:
        template (str): The HTML template content as a string.
        replacement (str): The string to replace the placeholder with.

    Returns:
        str: The modified HTML content with the placeholder replaced.
    """

    return template.replace("__REPLACE_ANIMALS_INFO__", replacement)


def main():
    """The main function to execute the entire process.

    This function calls the necessary functions to load animal data, generate HTML content,
    replace the placeholder in the template, and potentially write the result to a new file.

    You can modify this function to suit your specific needs, such as writing the output to a file.
    """

    template_content = read_template()
    animal_info = generate_animals_info()
    replaced_template = replace_placeholder(template_content, animal_info)

    print(replaced_template)


if __name__ == "__main__":
    main()

