# Chart rendering components

# Funnel chart
# - render_funnel_chart(data: dict)
#   Expected payload: {"stages": [{"name": str, "count": int}], "conversion_rates": [float]}
# - display conversion funnel visualization
# - show stage-by-stage breakdown

# Trend chart
# - render_trend_chart(data: list, x_col: str, y_col: str)
#   Expected payload: [{"date": str, "browse": int, "cart": int, "checkout": int, "purchase": int}]
# - display time-series trends
# - support multiple metrics overlay

# Drop-off chart
# - render_dropoff_chart(data: dict)
#   Expected payload: {"stages": [{"from": str, "to": str, "dropoff_rate": float}], "critical_points": [str]}
# - visualize drop-off points
# - highlight critical drop-off stages
