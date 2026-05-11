import requests
from config.settings import BACKEND_BASE_URL

# Request session setup
session = requests.Session()
session.headers.update({"Content-Type": "application/json"})

# Base URL loading
BASE_URL = BACKEND_BASE_URL

# GET request handling
def _get(endpoint, params=None):
    """Handle GET requests to the backend API."""
    url = f"{BASE_URL}{endpoint}"
    try:
        response = session.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e), "endpoint": endpoint}

# Response parsing helpers
def parse_funnel_response(response):
    """Parse funnel summary response."""
    if "error" in response:
        return None
    return response.get("data", {})

def parse_conversion_response(response):
    """Parse conversion summary response."""
    if "error" in response:
        return None
    return response.get("data", {})

def parse_trend_response(response):
    """Parse trend data response."""
    if "error" in response:
        return None
    return response.get("data", [])

def parse_dropoff_response(response):
    """Parse drop-off analysis response."""
    if "error" in response:
        return None
    return response.get("data", {})

def parse_stage_leakage_response(response):
    """Parse stage leakage response."""
    if "error" in response:
        return None
    return response.get("data", [])

def parse_behavior_response(response):
    """Parse behavior insights response."""
    if "error" in response:
        return None
    return response.get("data", {})

def parse_abandonment_response(response):
    """Parse abandonment summary response."""
    if "error" in response:
        return None
    return response.get("data", {})

def parse_experiments_response(response):
    """Parse experiments response."""
    if "error" in response:
        return None
    return response.get("data", [])

def parse_recommendations_response(response):
    """Parse recommendations response."""
    if "error" in response:
        return None
    return response.get("data", [])

# API client functions

def health_check():
    """Check backend health status."""
    return _get("/health")

def get_funnel_summary(filters=None):
    """Fetch funnel summary data (browse → cart → checkout → purchase)."""
    # Request: GET /funnel/summary?date_range=...&device=...
    # Response parsing: parse_funnel_response()
    response = _get("/funnel/summary", params=filters)
    return parse_funnel_response(response)

def get_conversion_summary(filters=None):
    """Fetch conversion summary data (KPI metrics)."""
    # Request: GET /conversion/summary?date_range=...&device=...
    # Response parsing: parse_conversion_response()
    response = _get("/conversion/summary", params=filters)
    return parse_conversion_response(response)

def get_trend_data(filters=None):
    """Fetch trend data for time-series visualization."""
    # Request: GET /funnel/trends?date_range=...&device=...
    # Response parsing: parse_trend_response()
    response = _get("/funnel/trends", params=filters)
    return parse_trend_response(response)

def get_dropoff_trend(filters=None):
    """Fetch dropoff trend data over time."""
    # Request: GET /dropoff/trends?date_range=...&device=...
    # Response parsing: parse_trend_response()
    response = _get("/dropoff/trends", params=filters)
    return parse_trend_response(response)

def get_behavior_trend(filters=None):
    """Fetch behavior metrics trend data over time."""
    # Request: GET /behavior/trends?date_range=...&device=...
    # Response parsing: parse_trend_response()
    response = _get("/behavior/trends", params=filters)
    return parse_trend_response(response)

def get_dropoff_summary(filters=None):
    """Fetch drop-off analysis data."""
    # Request: GET /dropoff/summary?date_range=...&device=...
    # Response parsing: parse_dropoff_response()
    response = _get("/dropoff/summary", params=filters)
    return parse_dropoff_response(response)

def get_stage_leakage(filters=None):
    """Fetch stage leakage data (user loss between funnel stages)."""
    # Request: GET /dropoff/stage-leakage?date_range=...&device=...
    # Response parsing: parse_stage_leakage_response()
    response = _get("/dropoff/stage-leakage", params=filters)
    return parse_stage_leakage_response(response)

def get_behavior_summary(filters=None):
    """Fetch user behavior insights."""
    # Request: GET /behavior/summary?date_range=...&device=...
    # Response parsing: parse_behavior_response()
    response = _get("/behavior/summary", params=filters)
    return parse_behavior_response(response)

def get_abandonment_summary(filters=None):
    """Fetch abandonment summary data (cart/checkout abandonment patterns)."""
    # Request: GET /behavior/abandonment?date_range=...&device=...
    # Response parsing: parse_abandonment_response()
    response = _get("/behavior/abandonment", params=filters)
    return parse_abandonment_response(response)

def get_experiments(status=None):
    """Fetch A/B testing experiments."""
    # Request: GET /experiments?status=...
    # Response parsing: parse_experiments_response()
    response = _get("/experiments", params={"status": status})
    return parse_experiments_response(response)

def get_recommendations(priority=None):
    """Fetch optimization recommendations."""
    # Request: GET /recommendations?priority=...
    # Response parsing: parse_recommendations_response()
    response = _get("/recommendations", params={"priority": priority})
    return parse_recommendations_response(response)

