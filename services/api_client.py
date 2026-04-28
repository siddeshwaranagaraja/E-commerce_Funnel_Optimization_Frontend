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

# Response parsing helpers
# - parse_funnel_response(response)
# - parse_dropoff_response(response)
# - parse_behavior_response(response)
# - parse_experiments_response(response)
# - parse_recommendations_response(response)

# API client functions

def health_check():
    """Check backend health status."""
    return _get("/health")

def get_funnel_summary(filters=None):
    """Fetch funnel summary data (browse → cart → checkout → purchase)."""
    # Request: GET /funnel/summary?date_range=...&device=...
    # Response parsing: parse_funnel_response()
    return _get("/funnel/summary", params=filters)

def get_dropoff_summary(filters=None):
    """Fetch drop-off analysis data."""
    # Request: GET /dropoff/summary?date_range=...&device=...
    # Response parsing: parse_dropoff_response()
    return _get("/dropoff/summary", params=filters)

def get_behavior_summary(filters=None):
    """Fetch user behavior insights."""
    # Request: GET /behavior/summary?date_range=...&device=...
    # Response parsing: parse_behavior_response()
    return _get("/behavior/summary", params=filters)

def get_experiments(status=None):
    """Fetch A/B testing experiments."""
    # Request: GET /experiments?status=...
    # Response parsing: parse_experiments_response()
    return _get("/experiments", params={"status": status})

def get_recommendations(priority=None):
    """Fetch optimization recommendations."""
    # Request: GET /recommendations?priority=...
    # Response parsing: parse_recommendations_response()
    return _get("/recommendations", params={"priority": priority})

