import json


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

def print_plant(zone_name, plant_name):
    # Safely lookup the zone (use .get())
    zone = garden.get(zone_name)
    # If zone exists:
    if zone:
        plant = zone.get(plant_name)
        # Safely lookup the plant inside that zone
        # If plant exists:
            # Print type, height, and main color
        if plant:
            print(f"Type: {plant['type']}")
            print(f"Height (ft): {plant['height_ft']}")
            print(f"Main Color: {plant['main_color']}")
        # Else:
        else:
            print(f"{plant_name} not found in {zone_name}")
            # Print "Plant not found in this zone."
    # Else:
    else:
        print("Zone not found.")
        # Print "Zone not found."

def update_plant_color(zone_name, plant_name, new_color):
    # Safely check if zone and plant exist
    zone = garden.get(zone_name)

    # If they exist:
    if zone:
        plant = zone.get(plant_name)
        if plant:
        # Update the plant's "main_color" attribute
            plant["main_color"] = new_color
            print(f"Updated {plant_name}'s color to {new_color}.")
        # Print confirmation
        else:
            print(f"{plant_name} was not found in {zone_name}")

    else:
        print(f"{zone_name} not found.")
    # Else:
        # Print appropriate error message
    save_garden_to_file(garden)

def update_plant_height(zone_name, plant_name, new_height):
    zone = garden.get(zone_name)
    if zone:
        plant = zone.get(plant_name)
        if plant:
            plant["height_ft"] = new_height
            print(f"Updated {plant_name}'s height to {new_height}.")
        else:
            print(f"{plant_name} was not found in {zone_name}")
    else:
        print(f"{zone_name} not found.")
    save_garden_to_file(garden)




def view_garden():
    for zone_name, plants in garden.items():
        print(f"Zone: {zone_name}")
        for plant_name, plant_info in plants.items():
            print(f"    {plant_name}")
            print(f"        Type: {plant_info['type']}")
            print(f"        Height (ft): {plant_info['height_ft']}")
            print(f"        Main Color: {plant_info['main_color']}")
            print()

def view_garden_options(garden):
    while True:
        print("View Options\n1. View Entire Garden\n2. View specific zone\n3. View specific plant\n4. Main Menu")
        choice = input("Enter choice (1-4): ")
        if choice == "1":
            view_garden()
        elif choice == "2":
            for zone_name, plants in garden.items():
                print(f"{zone_name}")
        elif choice == "3":
            zone_name = input("Which zone: ")
            zone = garden.get(zone_name)
            if not zone:
                print("Zone not found.")
                return
            else:
                plant_name = input("Which plant: ")
                plant = zone.get(plant_name)
                if not plant:
                    print("Plant not found.")
                    return
                else:
                    print(f"{plant_name}")
                    print(plant['type'])
                    print(plant['height_ft'])
                    print(plant['main_color'])
        elif choice == "4":
            menu()
        else:
            print("Invalid. Please choose (1-4)")



def save_garden_to_file(garden):
    file_path = r"C:\Users\STUPID TOES\OneDrive\Documents\garden.json"

    with open(file_path, "w") as f:
        json.dump(garden, f)

def load_garden_from_file():
    file_path = r"C:\Users\STUPID TOES\OneDrive\Documents\garden.json"
    try:
        with open(file_path, "r") as f:
            loaded_garden = json.load(f)
        return loaded_garden
    except FileNotFoundError:
        print("Error: File not found.")
        return{}
    except json.JSONDecodeError:
        return {}

def print_main_menu():
    print("1. View Garden.")
    print("2. Update plant color.")
    print("3. Update Plant Height.")
    print("4. Exit")



def handle_menu_choice():
    while True:
        try:
            print_main_menu()
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                view_garden_options(garden)

            elif choice == "2":
                zone_name = input("Enter the zone name: ")
                plant_name = input("Enter the plant name: ")
                new_color = input("Enter new color: ")
                update_plant_color(zone_name, plant_name, new_color)
            elif choice == "3":
                zone_name = input("Enter the zone name: ")
                plant_name = input("Enter the plant name: ")
                new_height = int(input("Enter new height: "))
                update_plant_height(zone_name, plant_name, new_height)
            elif choice == "4":
                print("Exiting Program")
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error: {e}")


garden = load_garden_from_file()
handle_menu_choice()
save_garden_to_file(garden)


