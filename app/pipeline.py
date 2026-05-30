from log_loader import load_logs_from_folder
from parsers import parse_log
from normalizer import normalize_log


def build_normalized_logs(folder_path):
    logs_data = load_logs_from_folder(folder_path)

    normalized_logs = []

    for file_data in logs_data:
        for raw_log in file_data["logs"]:
            parsed_log = parse_log(raw_log)
            normalized_log = normalize_log(parsed_log)

            if normalized_log is not None:
                normalized_logs.append(normalized_log)

    return normalized_logs


if __name__ == "__main__":
    logs = build_normalized_logs("logs")

    print("Total normalized logs:", len(logs))
    print("-" * 50)

    for log in logs:
        print(log)