import data_fetcher
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)


def read_template():
    """Reads the contents of the HTML template file.

    This function opens the 'animals_template.html' file in read mode and
    returns the entire content as a string.

    Returns:
        str: The content of the HTML template file.
    """
    with open('animals_template.html', 'r', encoding="utf-8") as content:
        return content.read()


def serialize_animal(animal_obj):
    """Generates HTML content for a single animal.

    This function takes a dictionary representing an animal and
    returns a string containing the HTML code for displaying that animal's
    information.
    """
    output = ''
    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal_obj["name"]}</div>\n'
    output += '<p class="card__text">\n'
    if 'diet' in animal_obj["characteristics"]:
        output += f'<strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n'
    output += f'<strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'
    if 'type' in animal_obj["characteristics"]:
        output += f'<strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n'
    output += '</p>\n'
    output += '</li>\n'
    return output


def generate_error_message(animal_name):
    """Generates an HTML string with an error message for a non-existent animal."""
    return f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'


def generate_animals_info(data, animal_name):
    """Generates HTML content for all animals or an error message."""
    output = ''
    if data:  # Check if data is not None (API call successful)
        for animal in data:
            output += serialize_animal(animal)
    else:
        output = generate_error_message(animal_name)  # Generate error message
    return output


def replace_placeholder(template, replacement):
    """Replaces the placeholder text in the HTML template
    with the provided replacement string.
    """
    if replacement is None:
        replacement = ''
    return template.replace("__REPLACE_ANIMALS_INFO__", replacement)


def write_to_html_file(content):
    """This function takes the generated HTML content and writes it to a new file
    named 'animals.html' in write mode."""
    with open('animals.html', "w") as new_file:
        return new_file.write(content)


def main():
    """Main function to generate an HTML file displaying animal information.

        This function prompts the user to enter the name of an animal they want to know
        about, fetches the relevant data, processes it, and generates an HTML file
        named 'animals.html' displaying the information. If the animal is not found,
        an error message is displayed instead.
    """
    print(Fore.CYAN + Style.BRIGHT + "Welcome to the Animal Information Generator!")
    animal_name = input(Fore.RED + "Enter animal you want to know: ")
    animals_data = data_fetcher.fetch_data(animal_name)
    template_content = read_template()
    content_to_replace = generate_animals_info(animals_data, animal_name)
    replaced_template = replace_placeholder(template_content, content_to_replace)
    write_to_html_file(replaced_template)
    print(Fore.YELLOW + Style.BRIGHT + "it's all done. Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
