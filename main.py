import animals_web_generator

HTML_FILE_NAME = 'animals_template.html'

def main():
    """
    Generates an animal information website using data fetched from the web.

    This function serves as the entry point for the program. It performs the following steps:

    1. Gets user input for the animal to display information about.
    2. Fetches animal data from the web using the `animals_web_generator.handle_fetcher_response` function.
    3. Reads the existing HTML template from a file (`HTML_FILE_NAME`).
    4. Replaces a placeholder string ("__REPLACE_ANIMALS_INFO__") in the HTML with the fetched animal data.
    5. Writes the modified HTML content to a new file named "animals.html".
    6. Prints a success message indicating the generated website file.

    This function relies on the following functions from the `animals_web_generator` module:
        - get_user_input
        - handle_fetcher_response (assumed to be defined elsewhere)
        - read_html
        - write_new_html
    """
    animal = animals_web_generator.get_user_input()
    animals_data = animals_web_generator.handle_fetcher_response(animal)
    html_string = animals_web_generator.read_html(HTML_FILE_NAME)
    # animal_info = animals_web_generator.all_animal_info(animals_data)
    new_html_data = html_string.replace("__REPLACE_ANIMALS_INFO__", animals_data)
    animals_web_generator.write_new_html(new_html_data, "animals.html")
    print(f"Website was successfully generated to the file {HTML_FILE_NAME}")
  

if __name__ == "__main__":
    main()
