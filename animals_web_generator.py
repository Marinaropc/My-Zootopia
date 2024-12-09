import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def organize_data(animals_data):
    output= ''
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
            output += (f"Name: {animal_name}\nDiet: {animal_diet}"
               f"\nLocation: {animal_location}\n")
        else:
            output += (f"Name: {animal_name}\nDiet: {animal_diet}"
                f"\nLocation: {animal_location}\nType: {animal_type}\n")
    return output

def rewrite_html(animals_info, template, output_file):
    with open(template, "r") as fileobj:
        template = fileobj.read()

    new_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    with open(output_file, "w") as fileobj:
        fileobj.write(new_html)


def main():
    animals_info = load_data("animals_data.json")
    animals_string = organize_data(animals_info)
    rewrite_html(animals_string,"animals_template.html", "animals.html")
    print (animals_string)


if __name__ == "__main__":
    main()