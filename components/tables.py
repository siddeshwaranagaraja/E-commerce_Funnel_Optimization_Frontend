# Table display components
from typing import List, Dict

def render_insights_table(data: List[Dict]):
    """
    Render insights table with user behavior insights.
    """
    # placeholder: implement insights table rendering
    return {
        "type": "table",
        "columns": ["insight_type", "description", "confidence", "action"],
        "data": data,
        "sortable": True,
        "filterable": True,
    }

def render_recommendations_table(data: List[Dict]):
    """
    Render recommendations table with optimization suggestions.
    """
    # placeholder: implement recommendations table rendering
    return {
        "type": "table",
        "columns": ["recommendation", "priority", "impact", "effort", "action"],
        "data": data,
        "sortable": True,
        "filterable": True,
        "row_colors": lambda row: "red" if row.get("priority") == "high" else "yellow" if row.get("priority") == "medium" else "green"
    }

def render_funnel_summary_table(data: List[Dict]):
    """
    Render funnel summary table.
    Columns: stage, count, conversion_rate, comparison
    """
    # placeholder: implement funnel summary table rendering
    return {
        "type": "table",
        "columns": ["stage", "user_count", "session_count", "conversion_rate", "comparison"],
        "data": data,
        "sortable": True,
        "filterable": False,
    }

def render_dropoff_comparison_table(data: List[Dict]):
    """
    Render dropoff comparison table.
    Expected payload: [{"from_stage": str, "to_stage": str, "from_count": int, "to_count": int, "dropoff_count": int, "dropoff_rate": float}]
    """
    if not data:
        return {"type": "error", "message": "No dropoff data available"}
    
    # Transform data for display
    table_data = []
    for row in data:
        dropoff_rate = row.get("dropoff_rate", 0)
        table_data.append({
            "from_stage": row.get("from_stage", ""),
            "to_stage": row.get("to_stage", ""),
            "from_count": row.get("from_count", 0),
            "to_count": row.get("to_count", 0),
            "dropoff_count": row.get("dropoff_count", 0),
            "dropoff_rate": f"{dropoff_rate:.2f}%",
            "conversion_rate": f"{(100 - dropoff_rate):.2f}%"
        })
    
    return {
        "type": "table",
        "columns": ["from_stage", "to_stage", "from_count", "to_count", "dropoff_count", "dropoff_rate", "conversion_rate"],
        "data": table_data,
        "sortable": True,
        "filterable": True,
        "row_styles": {
            "dropoff_rate": lambda rate: "critical" if float(rate.rstrip('%')) > 40 else "warning" if float(rate.rstrip('%')) > 20 else "normal"
        }
    }

def render_segment_comparison_table(data: Dict[str, List[Dict]], segment_type: str = "device_type"):
    """
    Render segment-based dropoff comparison table.
    """
    # placeholder: implement segment comparison table rendering
    return {
        "type": "table",
        "segment_type": segment_type,
        "segments": list(data.keys()),
        "data": data,
        "sortable": True,
        "filterable": True,
    }


def render_behavior_pattern_table(data: List[Dict]):
    """
    Render behavior pattern summary table.
    Expected payload: [{"pattern": str, "user_count": int, "avg_sessions": float,
                        "conversion_rate": float, "dominant_device": str, "trend": str}]
    """
    if not data:
        return {"type": "error", "message": "No behavior pattern data available"}

    table_data = []
    for row in data:
        conversion_rate = row.get("conversion_rate", 0)
        table_data.append({
            "pattern": row.get("pattern", ""),
            "user_count": row.get("user_count", 0),
            "avg_sessions": f"{row.get('avg_sessions', 0):.1f}",
            "conversion_rate": f"{conversion_rate:.2f}%",
            "dominant_device": row.get("dominant_device", "N/A"),
            "trend": row.get("trend", "stable")
        })

    return {
        "type": "table",
        "columns": ["pattern", "user_count", "avg_sessions", "conversion_rate", "dominant_device", "trend"],
        "data": table_data,
        "sortable": True,
        "filterable": True,
        "row_styles": {
            "trend": lambda t: "positive" if t == "up" else "negative" if t == "down" else "neutral"
        }
    }


def render_insight_summary_table(data: List[Dict]):
    """
    Render insight summary table.
    Expected payload: [{"stage": str, "issue": str, "severity": str, "recommendation": str, "impact": float}]
    """
    if not data:
        return {"type": "error", "message": "No insight data available"}

    table_data = []
    for row in data:
        impact = row.get("impact", 0)
        table_data.append({
            "stage": row.get("stage", ""),
            "issue": row.get("issue", ""),
            "severity": row.get("severity", "info").upper(),
            "impact": f"{impact:.1f}%",
            "recommendation": row.get("recommendation", "")[:50] + ".." if len(row.get("recommendation", "")) > 50 else row.get("recommendation", "")
        })

    return {
        "type": "table",
        "columns": ["stage", "issue", "severity", "impact", "recommendation"],
        "data": table_data,
        "sortable": True,
        "filterable": True,
        "row_styles": {
            "severity": lambda sev: "critical" if sev == "CRITICAL" else "warning" if sev == "WARNING" else "info"
        }
    }

