from data_fetcher import fetch_data


def user_input():
    user_choice = input("Type an animal: ")
    params = {"name": user_choice}
    return params


def organize_data(animals_data):
    """
    Iterate through the animals_data and return all 
    animal cards in an HTML-friendly format.

    Args:
        animals_data (list): List of animal dictionaries.

    Returns:
        str: HTML string containing animal cards.
    """
    animal_cards= ''
    for animal_dict in animals_data:
        try:
            animal_name = animal_dict["name"]
        except KeyError:
            animal_name = "Unknown"
        try:
            animal_diet = animal_dict["characteristics"]["diet"]
        except KeyError:
            animal_diet = "Unknown"
        try:
            animal_location = animal_dict["locations"][0]
        except KeyError:
            animal_location = "Unknown"
        try:
            animal_type = animal_dict["characteristics"]["type"]
        except KeyError:
            animal_type = "Unknown"
        if animal_type == "Unknown":
            animal_cards += f"""<li class="cards__item">\n
                        <div class="card__title">{animal_name}</div>\n
                        <p class="card__text">\n
                        <strong>Diet:</strong> {animal_diet}<br/>\n
                        <strong>Location:</strong> {animal_location}<br/>\n
                        </p>\n
                        </li>\n"""
        else:
            animal_cards += f"""<li class="cards__item">\n
                        <div class="card__title">{animal_name}</div>\n
                        <p class="card__text">\n
                        <strong>Diet:</strong> {animal_diet}<br/>\n
                        <strong>Location:</strong> {animal_location}<br/>\n
                        <strong>Type:</strong> {animal_type}<br/>\n
                        </p>\n
                        </li>\n"""
    return animal_cards


def rewrite_html(animals_info, template, output_file):
    """
    Read a template and create a new file with updated animal data.

    Args:
        animals_info (str): HTML-formatted animal cards.
        template (str): Path to the template file.
        output_file (str): Path to the output HTML file.
    """

    with open(template, "r") as fileobj:
        template_content = fileobj.read()

    if not animals_info.strip():
        animals_info = """
        <li class="cards__item">
            <div class="card__title">Animal Not Found</div>
            <p class="card__text">The animal you searched for is not available in the database.</p>
        </li>
        """

    new_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    with open(output_file, "w") as fileobj:
        fileobj.write(new_html)

def main():
    """ Takes care of executing all functions """
    params = user_input()
    api_data = fetch_data(params)
    if api_data and len(api_data)>0:
        animals_string = organize_data(api_data)
    else:
        animals_string = ""
    rewrite_html(animals_string,
                 "animals_template.html",
            "animals.html")


if __name__ == "__main__":
    main()