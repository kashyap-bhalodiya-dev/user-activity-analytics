def detect_anomalies(analytics):
    anomalies = []

    drop_off_points = analytics.get("drop_off_points", {})
    drop_offs = drop_off_points.get("drop_offs", {})

    for drop_name, drop_data in drop_offs.items():
        drop_percentage = drop_data.get("drop_percentage", 0)

        if drop_percentage >= 50:
            anomalies.append({
                "type": "high_drop_off",
                "severity": "high",
                "message": f"High drop-off detected at {drop_name}: {drop_percentage}% users dropped."
            })

    most_visited_pages = analytics.get("most_visited_pages", {})

    pricing_visits = most_visited_pages.get("pricing", 0)
    checkout_visits = most_visited_pages.get("checkout", 0)

    if pricing_visits > 0:
        checkout_ratio = checkout_visits / pricing_visits

        if checkout_ratio < 0.5:
            anomalies.append({
                "type": "low_checkout_traffic",
                "severity": "medium",
                "message": f"Checkout traffic is low compared to pricing. Checkout received {checkout_visits} visits while pricing received {pricing_visits} visits."
            })

    most_clicked_elements = analytics.get("most_clicked_elements", {})

    if most_clicked_elements:
        total_clicks = sum(most_clicked_elements.values())
        top_element = max(most_clicked_elements, key=most_clicked_elements.get)
        top_clicks = most_clicked_elements[top_element]

        if total_clicks > 0:
            click_share = top_clicks / total_clicks

            if click_share >= 0.4:
                anomalies.append({
                    "type": "dominant_clicked_element",
                    "severity": "low",
                    "message": f"'{top_element}' received {round(click_share * 100, 2)}% of all clicks, which may indicate strong user focus on this element."
                })

    return anomalies