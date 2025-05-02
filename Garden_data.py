import json


# -------------------------------
# Load garden data from a JSON file
# -------------------------------
def load_garden_from_file():
    file_path = "garden.json"
    try:
        with open(file_path, "r") as f:
            loaded_garden = json.load(f)
        return loaded_garden
    except FileNotFoundError:
        print("Error: File not found. Starting with default garden.")
        return {}
    except json.JSONDecodeError:
        print("Error: Corrupted file. Starting with default garden.")
        return {}


# -------------------------------
# Save garden data to a JSON file
# -------------------------------
def save_garden_to_file(garden):
    file_path = "garden.json"
    with open(file_path, "w") as f:
        json.dump(garden, f)

