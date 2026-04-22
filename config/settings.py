from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

FRONTEND_APP_TITLE = "E-commerce Funnel Optimization"
BACKEND_BASE_URL = "https://api.example.com"
DEFAULT_FILTERS = {
    "date_range": "last_30_days",
    "device": "all",
    "event_types": ["browse", "cart", "checkout", "purchase"],
}

# dotenv support can be added for local environment variables

