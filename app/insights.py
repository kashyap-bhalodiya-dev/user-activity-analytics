def generate_insights(analytics):
    insights = []

    most_visited_pages = analytics.get("most_visited_pages", {})
    most_clicked_elements = analytics.get("most_clicked_elements", {})
    event_frequency = analytics.get("event_frequency", {})
    drop_off_points = analytics.get("drop_off_points", {})

    if most_visited_pages:
        top_page = max(most_visited_pages, key=most_visited_pages.get)
        top_page_count = most_visited_pages[top_page]

        insights.append(
            f"The most visited page is '{top_page}' with {top_page_count} visits."
        )

    if most_clicked_elements:
        top_element = max(most_clicked_elements, key=most_clicked_elements.get)
        top_element_count = most_clicked_elements[top_element]

        insights.append(
            f"The most clicked element is '{top_element}' with {top_element_count} clicks."
        )

    if event_frequency:
        total_events = sum(event_frequency.values())

        insights.append(
            f"A total of {total_events} events were recorded."
        )

    drop_offs = drop_off_points.get("drop_offs", {})

    if drop_offs:
        highest_drop_name = None
        highest_drop_percentage = -1

        for drop_name, drop_data in drop_offs.items():
            drop_percentage = drop_data.get("drop_percentage", 0)

            if drop_percentage > highest_drop_percentage:
                highest_drop_percentage = drop_percentage
                highest_drop_name = drop_name

        if highest_drop_name is not None:
            drop_data = drop_offs[highest_drop_name]

            insights.append(
                f"The biggest drop-off is '{highest_drop_name}' with a {drop_data['drop_percentage']}% drop. "
                f"{drop_data['drop_count']} users/views dropped between these steps."
            )

    return insights