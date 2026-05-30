def clean_page_name(page):
    if page is None:
        return None

    page = page.strip()

    if page.startswith("/"):
        page = page[1:]

    return page


def normalize_log(parsed_log):
    if parsed_log is None:
        return None

    return {
        "user_id": int(parsed_log.get("user_id")) if parsed_log.get("user_id") is not None else None,
        "event": parsed_log.get("event"),
        "page": clean_page_name(parsed_log.get("page")),
        "element": parsed_log.get("element"),
        "timestamp": parsed_log.get("timestamp")
    }