This is a simple console application that helps manage a virtual garden. Plants are grouped by zones, and you can view, update, or add to your garden. It was built as a hands-on project to practice Python, especially working with nested dictionaries, file handling, and organizing code across multiple files.

What It Does
View the entire garden or look at specific zones or plants

Add new zones or plants

Update a plant’s color or height

Automatically saves all changes to a JSON file

Why I Made It
I wanted a project that helped me actually use what I’ve been learning in Python. This one gave me real practice with:

Working with nested dictionaries

Saving and loading structured data using the json module

Organizing code using functions and modules

Validating user input and handling errors

Designing a usable menu system

File Overview
php
Copy
Edit
garden/
├── main.py             # Starts the program
├── garden_data.py      # Loads and saves garden.json
├── garden_menus.py     # Displays the menu and handles user input
├── garden_core.py      # Core logic for garden actions
├── default.py          # Fallback default garden if no file is found
└── garden.json         # Saved garden data
How to Run
Make sure you have Python installed.

Run the program with:

bash
Copy
Edit
python main.py
If garden.json doesn't exist, it will use the default layout from default.py. Any updates you make are saved automatically.
