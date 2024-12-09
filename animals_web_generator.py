import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)
    
animals_info = load_data("animals_data.json")


def print_data(animals_data):
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
            print (f"Name: {animal_name}\nDiet: {animal_diet}"
               f"\nLocation: {animal_location}\n")
        else:
            print (f"Name: {animal_name}\nDiet: {animal_diet}"
                f"\nLocation: {animal_location}\nType: {animal_type}\n")

print_data(animals_info)