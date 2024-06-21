import data_fetcher


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


def handle_fetcher_response(animal):
    """
    Processes the response from the data fetcher for a given animal.

    Args:
        animal (str): The name of the animal to process data for.

    Returns:
        str: A message indicating the result of the data fetch operation.
            - If the animal data doesn't exist, it returns a message stating 
                that the animal doesn't exist.
            - If the data fetcher returns an error tuple, it formats an error 
                message with the error code and message.
            - If the data fetch is successful, it calls the `all_animal_info` 
                function to format the complete animal information 
                (assuming this function exists).

    """
    responce = data_fetcher.fetch_data(animal)
    if responce == []:
        return f"The animal {animal} doesn't exist"
    elif type(responce) == tuple:
        return f"Error: {responce[0]}, error message: {responce[1]['error']}"
    else:
        return all_animal_info(responce)


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
            print("Please, enter a name of the animal. \n")
            animal = input("Enter here: ")
            new_animal = ''
            if animal[0].islower():
                    new_animal = animal[0].upper() + animal[1:]
                    return new_animal
            else:
                return animal
        except ValueError as e:
            print("You entered something that not an animal! Error: ", e)
