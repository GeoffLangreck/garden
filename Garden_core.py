
from Garden_data import save_garden_to_file


# -------------------------------
# Display a specific plant's details
# -------------------------------
def print_plant(garden, zone_name, plant_name):
    zone = garden.get(zone_name)
    if zone:
        plant = zone.get(plant_name)
        if plant:
            print(f"Type: {plant['type']}")
            print(f"Height (ft): {plant['height_ft']}")
            print(f"Main Color: {plant['main_color']}")
        else:
            print(f"{plant_name} not found in {zone_name}.")
    else:
        print("Zone not found.")


# -------------------------------
# Update the height of a plant
# -------------------------------
def update_plant_height(garden, zone_name, plant_name, new_height):
    zone = garden.get(zone_name)
    if zone:
        plant = zone.get(plant_name)
        if plant:
            plant["height_ft"] = new_height
            print(f"Updated {plant_name}'s height to {new_height}.")
        else:
            print(f"{plant_name} was not found in {zone_name}.")
    else:
        print(f"{zone_name} not found.")
    save_garden_to_file(garden)

# -------------------------------
# Update the color of a plant
# -------------------------------
def update_plant_color(garden, zone_name, plant_name, new_color):
    zone = garden.get(zone_name)
    if zone:
        plant = zone.get(plant_name)
        if plant:
            plant["main_color"] = new_color
            print(f"Updated {plant_name}'s color to {new_color}.")
        else:
            print(f"{plant_name} was not found in {zone_name}.")
    else:
        print(f"{zone_name} not found.")
    save_garden_to_file(garden)

# -------------------------------
# Add zone to garden
# -------------------------------
def add_zone(garden):
    zone_name = input("Enter new zone: ").strip().title()
    if zone_name in garden:
        print(f"{zone_name} already exists.")
    else:
        garden[zone_name] = {}
        print(f"Zone '{zone_name}' has been added.")
        save_garden_to_file(garden)

def add_plant(garden):
    zone_name = input("Which zone would you like to add to?").strip().title()
    if zone_name not in garden:
        print(f"{zone_name} does not exist.")
        return

    new_plant = input("Enter plant name: ").strip().title()

    if new_plant in garden[zone_name]:
        print(f"{new_plant} already exists in {zone_name}.")
        return

    new_type = input("Enter plant type (e.g., tree, flower, fruit): ").strip()

    try:
        new_height = int(input("Enter plant height (ft): "))
    except ValueError:
        print("invalid height.")
        return

    new_color = input("Enter plant color: ").strip().lower()

    garden[zone_name][new_plant] = {
        "type": new_type,
        "height_ft": new_height,
        "main_color": new_color
    }

    print(f"{new_plant} added to {zone_name}.")
    save_garden_to_file(garden)





# -------------------------------
# Display the entire garden by zone
# -------------------------------
def view_garden(garden):
    for zone_name, plants in garden.items():
        print(f"Zone: {zone_name}")
        for plant_name, plant_info in plants.items():
            print(f"    {plant_name}")
            print(f"        Type: {plant_info['type']}")
            print(f"        Height (ft): {plant_info['height_ft']}")
            print(f"        Main Color: {plant_info['main_color']}")
            print()


# -------------------------------
# Submenu for viewing garden information
# -------------------------------
def view_garden_options(garden):
    while True:
        print("View Options\n1. View Entire Garden\n2. View Specific Zone\n3. View Specific Plant\n4. Main Menu")
        choice = input("Enter choice (1-4): ")

        if choice == "1":
            view_garden(garden)

        elif choice == "2":
            for zone_name in garden.keys():
                print(zone_name)

        elif choice == "3":
            zone_name = input("Which zone: ")
            zone = garden.get(zone_name)
            if not zone:
                print("Zone not found.")
                return
            plant_name = input("Which plant: ")
            plant = zone.get(plant_name)
            if not plant:
                print("Plant not found.")
                return
            print(f"{plant_name}")
            print(f"Type: {plant['type']}")
            print(f"Height (ft): {plant['height_ft']}")
            print(f"Main Color: {plant['main_color']}")

        elif choice == "4":
            return

        else:
            print("Invalid. Please choose (1-4)")

