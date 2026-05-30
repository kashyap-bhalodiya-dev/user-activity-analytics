from app.parsers import parse_custom_log, parse_firebase_log, parse_mixpanel_log, parse_posthog_log

def parse_log(log):
    if "event_name" in log and "screen" in log:
        return parse_firebase_log(log)

    elif "distinct_id" in log and "properties" in log and "$pathname" not in log["properties"]:
        return parse_mixpanel_log(log)

    elif "distinct_id" in log and "properties" in log and "$pathname" in log["properties"]:
        return parse_posthog_log(log)

    elif "uid" in log and "action" in log:
        return parse_custom_log(log)

    else:
        return None