import os
import json


def load_logs_from_folder(folder_path):
    all_logs = []

    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder not found: {folder_path}")

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".json"):
            file_path = os.path.join(folder_path, file_name)

            try:
                with open(file_path, "r") as file:
                    logs = json.load(file)

                    all_logs.append({
                        "file_name": file_name,
                        "logs": logs
                    })

            except json.JSONDecodeError:
                print(f"Skipping invalid JSON file: {file_name}")

    return all_logs