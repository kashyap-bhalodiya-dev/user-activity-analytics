def parse_firebase_log(log):
    return {
        "user_id": log.get("user_id"),
        "event": log.get("event_name"),
        "page": log.get("screen"),
        "element": log.get("button"),
        "timestamp": log.get("event_time")
    }


def parse_mixpanel_log(log):
    properties = log.get("properties", {})

    return {
        "user_id": log.get("distinct_id"),
        "event": log.get("event"),
        "page": properties.get("page"),
        "element": properties.get("element"),
        "timestamp": properties.get("time")
    }


def parse_posthog_log(log):
    properties = log.get("properties", {})

    event_name = log.get("event")

    if event_name == "$pageview":
        event_name = "page_view"
    elif event_name == "$autocapture":
        event_name = "click"

    return {
        "user_id": log.get("distinct_id"),
        "event": event_name,
        "page": properties.get("$pathname"),
        "element": properties.get("element"),
        "timestamp": log.get("timestamp")
    }


def parse_custom_log(log):
    return {
        "user_id": log.get("uid"),
        "event": log.get("action"),
        "page": log.get("url"),
        "element": log.get("target"),
        "timestamp": log.get("created_at")
    }


def parse_log(log):
    properties = log.get("properties", {})

    if "event_name" in log and "screen" in log:
        return parse_firebase_log(log)

    elif "distinct_id" in log and "properties" in log and "$pathname" not in properties:
        return parse_mixpanel_log(log)

    elif "distinct_id" in log and "properties" in log and "$pathname" in properties:
        return parse_posthog_log(log)

    elif "uid" in log and "action" in log:
        return parse_custom_log(log)

    else:
        return None