import requests
from config.settings import BACKEND_BASE_URL

# Request session setup
session = requests.Session()
session.headers.update({"Content-Type": "application/json"})

# Base URL loading
BASE_URL = BACKEND_BASE_URL

# GET request handling placeholder
def _get(endpoint, params=None):
    """Handle GET requests to the backend API."""
    url = f"{BASE_URL}{endpoint}"
    # Placeholder for actual request handling
    return {"status": "pending", "endpoint": endpoint}

# API client functions

def health_check():
    """Check backend health status."""
    return _get("/health")

def get_funnel_summary(filters=None):
    """Fetch funnel summary data (browse → cart → checkout → purchase)."""
    return _get("/funnel/summary", params=filters)

def get_dropoff_summary(filters=None):
    """Fetch drop-off analysis data."""
    return _get("/dropoff/summary", params=filters)

def get_behavior_summary(filters=None):
    """Fetch user behavior insights."""
    return _get("/behavior/summary", params=filters)

def get_experiments(status=None):
    """Fetch A/B testing experiments."""
    return _get("/experiments", params={"status": status})

def get_recommendations(priority=None):
    """Fetch optimization recommendations."""
    return _get("/recommendations", params={"priority": priority})

