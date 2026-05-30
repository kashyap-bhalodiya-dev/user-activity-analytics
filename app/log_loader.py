import os
import json


def load_logs_from_folder(folder_path):
    all_logs = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".json"):
            file_path = os.path.join(folder_path, file_name)

            with open(file_path, "r") as file:
                logs = json.load(file)

                all_logs.append({
                    "file_name": file_name,
                    "logs": logs
                })

    return all_logs


if __name__ == "__main__":
    from parsers import parse_log
    from normalizer import normalize_log

    logs_data = load_logs_from_folder("logs")

    for file_data in logs_data:
        print("File:", file_data["file_name"])

        for log in file_data["logs"]:
            parsed_log = parse_log(log)
            normalized_log = normalize_log(parsed_log)

            print("Normalized Log:", normalized_log)

        print("-" * 50)