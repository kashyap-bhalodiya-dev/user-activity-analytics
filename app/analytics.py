import pandas as pd


def get_most_visited_pages(logs):
    df = pd.DataFrame(logs)

    page_views = df[df["event"] == "page_view"]

    result = page_views["page"].value_counts().to_dict()

    return result


def get_most_clicked_elements(logs):
    df = pd.DataFrame(logs)

    clicks = df[df["event"] == "click"]

    result = clicks["element"].value_counts().to_dict()

    return result


def get_event_frequency(logs):
    df = pd.DataFrame(logs)

    result = df["event"].value_counts().to_dict()

    return result


def get_drop_off_points(logs):
    df = pd.DataFrame(logs)

    page_views = df[df["event"] == "page_view"].copy()

    page_views["timestamp"] = pd.to_datetime(page_views["timestamp"])

    page_views = page_views.sort_values(by=["user_id", "timestamp"])

    funnel_steps = ["home", "pricing", "checkout"]

    funnel_counts = {
        "home": 0,
        "pricing": 0,
        "checkout": 0
    }

    users = page_views["user_id"].unique()

    for user_id in users:
        user_events = page_views[page_views["user_id"] == user_id]

        current_step_index = 0

        for _, event_row in user_events.iterrows():
            current_page = event_row["page"]

            expected_step = funnel_steps[current_step_index]

            if current_page == expected_step:
                reached_step = funnel_steps[current_step_index]
                funnel_counts[reached_step] += 1

                current_step_index += 1

                if current_step_index == len(funnel_steps):
                    break

    drop_offs = {}

    for i in range(len(funnel_steps) - 1):
        current_step = funnel_steps[i]
        next_step = funnel_steps[i + 1]

        current_count = funnel_counts[current_step]
        next_count = funnel_counts[next_step]

        drop_count = current_count - next_count

        if current_count > 0:
            drop_percentage = round((drop_count / current_count) * 100, 2)
        else:
            drop_percentage = 0

        drop_offs[f"{current_step}_to_{next_step}"] = {
            "from_count": current_count,
            "to_count": next_count,
            "drop_count": drop_count,
            "drop_percentage": drop_percentage
        }

    return {
        "funnel_counts": funnel_counts,
        "drop_offs": drop_offs
    }


def generate_analytics(logs):
    analytics = {
        "most_visited_pages": get_most_visited_pages(logs),
        "most_clicked_elements": get_most_clicked_elements(logs),
        "event_frequency": get_event_frequency(logs),
        "drop_off_points": get_drop_off_points(logs)
    }

    return analytics