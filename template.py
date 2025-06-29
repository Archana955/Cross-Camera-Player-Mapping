# setup_project.py

import os

# define your main project folder
project_root = "cross_camera_reid"

folders = [
    "videos",
    "models",
    "crop_embeddings/broadcast",
    "crop_embeddings/tacticam",
    "outputs"
]

for folder in folders:
    full_path = os.path.join(project_root, folder)
    os.makedirs(full_path, exist_ok=True)
    print(f"Created folder: {full_path}")

# create blank starter files
starter_files = [
    "main.py",
    "app.py",                  # for Flask integration later
    "utils.py",
    "extract_embeddings.py",
    "match_embeddings.py",
    "visualize_matches.py",
    "requirements.txt"
]

for file in starter_files:
    file_path = os.path.join(project_root, file)
    with open(file_path, "w") as f:
        pass  # creates an empty file
    print(f"Created file: {file_path}")

print("\nProject structure initialized successfully.")

