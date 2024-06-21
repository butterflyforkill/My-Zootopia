import animals_web_generator

HTML_FILE_NAME = 'animals_template.html'

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
    
    animal = animals_web_generator.get_user_input()
    animals_data = animals_web_generator.handle_fetcher_response(animal)
    html_string = animals_web_generator.read_html(HTML_FILE_NAME)
    animal_info = animals_web_generator.all_animal_info(animals_data)
    new_html_data = html_string.replace("__REPLACE_ANIMALS_INFO__", animal_info)
    animals_web_generator.write_new_html(new_html_data, "animals.html")
    print(f"Website was successfully generated to the file {HTML_FILE_NAME}")
  

if __name__ == "__main__":
    main()
