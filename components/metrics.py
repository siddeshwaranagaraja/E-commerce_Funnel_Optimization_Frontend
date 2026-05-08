# KPI and metric display components
from typing import Optional

# KPI cards
# - render_kpi_card(title, value, delta=None)
# - display single metric with optional change indicator
# - support for percentage and absolute values

# Summary blocks
# - render_summary_block(metrics_dict)
# - display multiple KPIs in a row
# - grid layout for dashboard sections

# Specific metric cards
# - render_browse_count(count, delta=None)
# - render_cart_count(count, delta=None)
# - render_checkout_count(count, delta=None)
# - render_purchase_count(count, delta=None)
# - render_overall_conversion(conversion_rate, delta=None)


def render_repeated_browsers(count: int, delta: Optional[float] = None):
    """
    Render card for users who browsed multiple times without converting.
    Expected payload: {"count": int, "delta": float}
    """
    return {
        "title": "Repeated Browsers",
        "value": count,
        "delta": delta,
        "help": "Users who browsed more than once without adding to cart",
        "icon": "🔁"
    }


def render_abandoned_carts(count: int, rate: float, delta: Optional[float] = None):
    """
    Render card for users who added to cart but did not proceed to checkout.
    Expected payload: {"count": int, "rate": float, "delta": float}
    """
    return {
        "title": "Abandoned Carts",
        "value": count,
        "subtext": f"{rate:.2f}% abandonment rate",
        "delta": delta,
        "help": "Users who added items to cart but did not reach checkout",
        "icon": "🛒"
    }


def render_checkout_exits(count: int, rate: float, delta: Optional[float] = None):
    """
    Render card for users who reached checkout but did not complete purchase.
    Expected payload: {"count": int, "rate": float, "delta": float}
    """
    return {
        "title": "Checkout Exits",
        "value": count,
        "subtext": f"{rate:.2f}% exit rate",
        "delta": delta,
        "help": "Users who reached checkout but did not complete the purchase",
        "icon": "🚪"
    }


def render_purchase_completion(count: int, rate: float, delta: Optional[float] = None):
    """
    Render card for users who completed the purchase.
    Expected payload: {"count": int, "rate": float, "delta": float}
    """
    return {
        "title": "Purchase Completions",
        "value": count,
        "subtext": f"{rate:.2f}% completion rate",
        "delta": delta,
        "help": "Users who successfully completed a purchase",
        "icon": "✅"
    }

