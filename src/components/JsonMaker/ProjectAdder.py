import tkinter as tk
import json
import os

def generate_json():
    # Get input values from the user
    id_value = id_entry.get()
    title_value = title_entry.get()
    date_value = date_entry.get()
    description_value = description_entry.get("1.0", tk.END).strip()
    image_value = image_entry.get()
    
    # Split tags and remove extra whitespaces
    tags_value = [tag.strip() for tag in tags_entry.get().split(",")]

    category_value = category_entry.get()
    github_value = github_entry.get()
    webapp_value = webapp_entry.get()

    # Create a dictionary with the collected data
    data = {
        "id": int(id_value),
        "title": title_value,
        "date": date_value,
        "description": description_value,
        "image": image_value,
        "tags": tags_value,
        "category": category_value,
        "github": github_value,
        "webapp": webapp_value
    }

    # Convert the dictionary to JSON format
    json_data = json.dumps(data, indent=2)

    # Save the JSON data to a file in the current folder as "Project.json"
    with open(os.path.join(os.getcwd(), "Project.json"), "w") as json_file:
        json_file.write(json_data)

# Create the main window
window = tk.Tk()
window.title("JSON Generator")

# Create and place input fields and labels
id_label = tk.Label(window, text="ID:")
id_label.grid(row=0, column=0)
id_entry = tk.Entry(window)
id_entry.grid(row=0, column=1)

title_label = tk.Label(window, text="Title:")
title_label.grid(row=1, column=0)
title_entry = tk.Entry(window)
title_entry.grid(row=1, column=1)

date_label = tk.Label(window, text="Date:")
date_label.grid(row=2, column=0)
date_entry = tk.Entry(window)
date_entry.grid(row=2, column=1)

description_label = tk.Label(window, text="Description:")
description_label.grid(row=3, column=0)
description_entry = tk.Text(window, height=5, width=30)
description_entry.grid(row=3, column=1)

image_label = tk.Label(window, text="Image URL:")
image_label.grid(row=4, column=0)
image_entry = tk.Entry(window)
image_entry.grid(row=4, column=1)

tags_label = tk.Label(window, text="Tags (comma-separated):")
tags_label.grid(row=5, column=0)
tags_entry = tk.Entry(window)
tags_entry.grid(row=5, column=1)

category_label = tk.Label(window, text="Category:")
category_label.grid(row=6, column=0)
category_entry = tk.Entry(window)
category_entry.grid(row=6, column=1)

github_label = tk.Label(window, text="GitHub URL:")
github_label.grid(row=7, column=0)
github_entry = tk.Entry(window)
github_entry.grid(row=7, column=1)

webapp_label = tk.Label(window, text="Web App URL:")
webapp_label.grid(row=8, column=0)
webapp_entry = tk.Entry(window)
webapp_entry.grid(row=8, column=1)

# Create a button to generate JSON
generate_button = tk.Button(window, text="Generate JSON", command=generate_json)
generate_button.grid(row=9, column=0, columnspan=2)

# Start the main event loop
window.mainloop()
