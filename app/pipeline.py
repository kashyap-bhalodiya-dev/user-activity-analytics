from app.log_loader import load_logs_from_folder
from app.parsers import parse_log
from app.normalizer import normalize_log


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
    from app.analytics import generate_analytics
    from app.insights import generate_insights

    logs = build_normalized_logs("logs")

    analytics = generate_analytics(logs)
    insights = generate_insights(analytics)

    print("Analytics:")
    print(analytics)

    print("\nInsights:")
    for insight in insights:
        print("-", insight)