import garden_core

# -------------------------------
# Display the main menu
# -------------------------------
def print_main_menu():
    print("Garden Viewer")
    print("1. View Garden")
    print("2. Update Plant Color")
    print("3. Update Plant Height")
    print()
    print("Zone & Plant Management")
    print("4. Add Zone")
    print("5. Add Plant")
    print()
    print("6. Exit")


# -------------------------------
# Handle main menu choices
# -------------------------------
def handle_menu_choice(garden):
    while True:
        try:
            print_main_menu()
            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                garden_core.view_garden_options(garden)
            elif choice == "2":
                zone_name = input("Enter the zone name: ")
                plant_name = input("Enter the plant name: ")
                new_color = input("Enter new color: ")
                garden_core.update_plant_color(zone_name, plant_name, new_color)
            elif choice == "3":
                zone_name = input("Enter the zone name: ")
                plant_name = input("Enter the plant name: ")
                new_height = int(input("Enter new height: "))
                garden_core.update_plant_height(zone_name, plant_name, new_height)
            elif choice == "4":
                garden_core.add_zone(garden)
            elif choice == "5":
                garden_core.add_plant(garden)
            elif choice == "6":
                print("Exiting program.")
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error: {e}")




