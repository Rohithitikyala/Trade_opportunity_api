def fetch_market_data(sector):
    data = {
        "technology": "AI growth, startups booming, cloud expansion",
        "pharmaceuticals": "New drug approvals, exports increasing",
        "agriculture": "Good monsoon, crop yield improved"
    }

    return data.get(sector.lower(), "Market stable with moderate growth")