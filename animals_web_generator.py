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
    Generates a string containing formatted information 
    for all animals in the provided data.

    Args:
        data (list): A list of dictionaries, where each 
        dictionary represents an animal with information.

    Returns:
        str: A string containing formatted information 
        for all animals, separated by newlines.
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
  
      
def handle_user_input(data, user_input):
    """
    Filters animal data based on the user's chosen skin type.

    This function takes a list of animal entries (dictionaries) 
    and the user's selected skin type (integer).
    It iterates through the animal data and creates 
    a new list containing only animals whose
    'skin_type' (within the 'characteristics' dictionary) 
    matches the user's input.

    Args:
        data (list): A list of dictionaries representing animal entries. 
            Each dictionary is assumed to have
            a sub-dictionary named 'characteristics' 
            containing a key 'skin_type' with an integer value.
        user_input (int): The user's chosen skin type as an integer.

    Returns:
        list: A new list containing animal entries (dictionaries) 
        that match the user's skin type preference.
    """
    new_data = []
    for animal in data:
        if user_input == animal['characteristics']['skin_type']:
            new_data.append(animal)
    return new_data


def get_user_input():
    """
    Prompts the user for their desired animal skin type and returns the input as an integer.

    This function repeatedly prompts the user until a valid integer input (1 or 2)
    is provided. It displays a menu with options for fur (1) and hair (2) skin types. 
    If the user enters a non-numeric value, a `ValueError` is raised, and an error message
    is displayed prompting the user to enter a valid number.

    Returns:
        string: The user's chosen skin type.
    """
    while True:
        try:
            print("Please, choose what animal skin type do you want: \n")
            print("- Fur; \n")
            print("- Hair; \n")
            skin_type = input("Enter here: ")
            new_skin_type = ''
            if skin_type[0].islower():
                    new_skin_type = skin_type[0].upper() + skin_type[1:]
                    return new_skin_type
            else:
                return skin_type
        except ValueError as e:
            print("You entered something that is not a number! Error: ", e)


def main():
    """
    Generates an HTML file containing 
    information about animals relevant to user's skin type.

    This function reads animal data from a JSON file, 
    prompts the user for their skin type,
    processes the animal data based on the 
    user input using the `handle_user_input` function,
    retrieves an HTML template, formats the animal 
    information, and replaces a placeholder
    in the template with the formatted information. 
    Finally, it writes the modified HTML content
    to a new HTML file.

    **Assumptions:**

        - The `load_data` function can load JSON data from a file.
        - The `get_user_input` function prompts the user 
            for their skin type and returns the input.
        - The `handle_user_input` function takes animal data and user skin type,
            and returns a potentially modified version of the animal data.
        - The `read_html` function can read HTML content from a file.
        - The `all_animal_info` function takes animal data 
            and returns formatted information.
        - The `write_new_html` function can write HTML content to a file.

    **Note:**

        - This function assumes the HTML template has 
            a placeholder named "__REPLACE_ANIMALS_INFO__".

    """
    animals_data = load_data('animals_data.json')
    skin_type = get_user_input()
    new_animals_data = handle_user_input(animals_data, skin_type)
    html_string = read_html('animals_template.html')
    animal_info = all_animal_info(new_animals_data)
    new_html_data = html_string.replace("__REPLACE_ANIMALS_INFO__", animal_info)
    write_new_html(new_html_data, "animals.html")
  

if __name__ == "__main__":
    main()
