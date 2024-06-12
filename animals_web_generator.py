import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def read_html(file_path):
    """Load HTML file

    Args:
        file_path: html file

    Returns:
        string: html file
    """
    with open(file_path, "r") as file:
        return file.read()


def animal_info(animal):
    """ 
    Returns string - information about a single animal.

    Args:
        animal (dict): A dictionary representing an animal entry.
    
    Returns:
        animal = string
    """
    characteristics = animal.get("characteristics", {})
    output = ''
    # Check if each field exists before printing
    if "name" in animal:
        output += "<div class='card__title'>"
        output += f"{animal['name']}<br/>\n"
        output += '</div>'
    output += '<p class="card__text"> <ul>'
    if "diet" in characteristics:
        output += '<li>'
        output += f"<strong>Diet:</strong> {characteristics['diet']}\n"
        output += '</li>'
    if "locations" in animal and animal["locations"]:  # Check for non-empty list
        output += '<li>'
        output += f"<strong>Location:</strong> {animal['locations'][0]}\n"
        output += '</li>'
    if "type" in characteristics:
        output += '<li>'
        output += f"<strong>Type:</strong> {characteristics['type']}\n" 
        output += '</li>'
    output += '</ul> </p>'    
    return output


def all_animal_info(data):
    """
    Generates a string containing formatted information for all animals in the provided data.

    Args:
        data (list): A list of dictionaries, where each dictionary represents an animal with information.

    Returns:
        str: A string containing formatted information for all animals, separated by newlines.
    """
    output = ''
    for animal in data:
        output += '<li class="cards__item">'
        output += animal_info(animal) + '\n'
        output += '</li>'
    return output


def write_new_html(data, html_name):
    """Write new html file with replaced animal data

    Args:
        data (string): animal data
        html_name (string): name of the file
    """
    with open(html_name, 'w') as file:
        file.write(data)


def main():
    """
    Generates an HTML file containing information about animals.

    This function reads animal data from a JSON file, retrieves an HTML template,
    formats the animal information, and replaces a placeholder in the template
    with the formatted information. Finally, it writes the modified HTML content
    to a new HTML file.

    **Assumptions:**

        - The `load_data` function can load JSON data from a file.
        - The `read_html` function can read HTML content from a file.
        - The `all_animal_info` function takes animal data and returns formatted information.
        - The `write_new_html` function can write HTML content to a file.

    **Note:**

        - This function assumes the HTML template has a placeholder named "__REPLACE_ANIMALS_INFO__".

    """
    animals_data = load_data('animals_data.json')
    html_string = read_html('animals_template.html')
    animal_info = all_animal_info(animals_data)
    new_html_data = html_string.replace("__REPLACE_ANIMALS_INFO__", animal_info)
    write_new_html(new_html_data, "animals.html")
  

if __name__ == "__main__":
    main()
