from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

FRONTEND_APP_TITLE = "E-commerce Funnel Optimization"
BACKEND_BASE_URL = "https://api.example.com"

# Time range defaults
TIME_RANGES = {
    "last_7_days": "Last 7 days",
    "last_30_days": "Last 30 days",
    "last_90_days": "Last 90 days",
}
DEFAULT_TIME_RANGE = "last_30_days"

# Page labels
PAGE_LABELS = {
    "funnel_overview": "Funnel Overview",
    "dropoff_analysis": "Drop-off Analysis",
    "behavior_insights": "Behavior Insights",
    "experiments": "Experiments",
    "recommendations": "Recommendations",
}

DEFAULT_FILTERS = {
    "date_range": DEFAULT_TIME_RANGE,
    "device": "all",
    "event_types": ["browse", "cart", "checkout", "purchase"],
}

# dotenv support can be added for local environment variables

