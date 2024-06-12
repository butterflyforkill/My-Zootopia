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
        output += f"Name: {animal['name']}<br/>\n"
    if "diet" in characteristics:
        output += f"Diet: {characteristics['diet']}<br/>\n"
    if "locations" in animal and animal["locations"]:  # Check for non-empty list
        output += f"Location: {animal['locations'][0]}<br/>\n"
    if "type" in characteristics:
        output += f"Type: {characteristics['type']}<br/>\n" 
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
    animals_data = load_data('animals_data.json')
    html_string = read_html('animals_template.html')
    animal_info = all_animal_info(animals_data)
    new_html_data = html_string.replace("__REPLACE_ANIMALS_INFO__", animal_info)
    write_new_html(new_html_data, "animals.html")
  

if __name__ == "__main__":
    main()
