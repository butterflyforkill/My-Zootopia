import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def print_animal_info(animal):
    """ 
    Prints information about a single animal.

    Args:
        animal (dict): A dictionary representing an animal entry.
    """
    characteristics = animal.get("characteristics", {})
    # Check if each field exists before printing
    if "name" in animal:
        print(f"Name: {animal['name']}")
    if "diet" in characteristics:
        print(f"Diet: {characteristics['diet']}")
    if "locations" in animal and animal["locations"]:  # Check for non-empty list
        print(f"Location: {animal['locations'][0]}")
    if "type" in characteristics:
        print(f"Type: {characteristics['type']}")
    print()  # Add a blank line between animals


def main():
    animals_data = load_data('My-Zootopia/animals_data.json')
    for animal in animals_data:
        print_animal_info(animal)


if __name__ == "__main__":
    main()
