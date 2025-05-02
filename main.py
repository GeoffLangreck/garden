
from Garden_data import load_garden_from_file, save_garden_to_file
from Garden_menus import handle_menu_choice




# -------------------------------
# Program entry point
# -------------------------------

if __name__ == "__main__":
    garden = load_garden_from_file()
    if not garden:
        # Default garden data (used if no file exists or file is empty)
        garden = {
        "North Zone": {
            "Pine": {
                "type": "tree",
                "height_ft": 40,
                 "main_color": "brown"
            },
            "Cactus": {
                "type": "flowering plant",
                "height_ft": 6,
                "main_color": "green"
            }
        },
        "West Zone": {
            "Rubber Tree": {
                "type": "tree",
                "height_ft": 12,
                "main_color": "beige"
            },
            "Diamicy": {
                "type": "flower",
                "height_ft": 1,
                "main_color": "red"
            }
        }
    }

    handle_menu_choice(garden)
    save_garden_to_file(garden)
