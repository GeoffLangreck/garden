import garden_data
import garden_menus
import default




# -------------------------------
# Program entry point
# -------------------------------

if __name__ == "__main__":
    garden = garden_data.load_garden_from_file()
    if not garden:
        # Default garden data (used if no file exists or file is empty)
        garden = default.default_garden

    garden_menus.handle_menu_choice(garden)
    garden_data.save_garden_to_file(garden)
