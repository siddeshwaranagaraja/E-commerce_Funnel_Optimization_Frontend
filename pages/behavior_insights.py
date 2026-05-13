import streamlit as st
from services import api_client
from components import tables

def main():
    st.set_page_title("Behavior Insights")

    st.title("🔍 Behavior Insights")

    # Sidebar filter placeholder
    st.sidebar.header("Filters")
    date_range = st.sidebar.selectbox("Date Range", ["Last 7 days", "Last 30 days", "Last 90 days"])
    device_filter = st.sidebar.multiselect("Device", ["All", "Mobile", "Desktop", "Tablet"], default="All")

    # Build filters dict for API calls
    filters = {
        "date_range": date_range,
        "device": device_filter
    }

    # Fetch behavior summary and abandonment data
    behavior_data = api_client.get_behavior_summary(filters=filters)
    abandonment_data = api_client.get_abandonment_summary(filters=filters)

    # Behavior pattern cards
    # Layout: row of cards for behavior metrics, trends, and patterns
    st.subheader("Behavior Patterns")
    card_col1, card_col2, card_col3 = st.columns(3)
    with card_col1:
        if behavior_data:
            st.metric("Avg Session Duration", behavior_data.get("avg_session_duration", "N/A"))
        else:
            st.info("Behavior metric card placeholder")
    with card_col2:
        if behavior_data:
            st.metric("Pages Per Session", behavior_data.get("pages_per_session", "N/A"))
        else:
            st.info("Behavior trend card placeholder")
    with card_col3:
        if abandonment_data:
            st.metric("Abandonment Rate", f"{abandonment_data.get('abandonment_rate', 0):.2f}%")
        else:
            st.info("Pattern summary card placeholder")

    # User segment table
    # Layout: table of segments, counts, conversion, and engagement
    st.subheader("User Segment Table")
    if behavior_data and behavior_data.get("segments"):
        st.json(behavior_data.get("segments"))  # Placeholder display
    else:
        st.info("User segment table placeholder will be displayed here.")

    # Anomaly section
    # Layout: anomaly detection summary and alerts
    st.subheader("Anomaly Detection")
    if behavior_data and behavior_data.get("anomalies"):
        st.json(behavior_data.get("anomalies"))  # Placeholder display
    else:
        st.info("Anomaly section placeholder for unusual behavior patterns will be displayed here.")

    # Fetch insights data
    insights_data = api_client.get_insight_summary(filters=filters)

    # Dedicated insight list section
    # Layout: list of behavioral insights with severity and actionability
    st.subheader("Behavioral Insights")
    if insights_data and isinstance(insights_data, list) and len(insights_data) > 0:
        # Display insights as expandable cards
        for idx, insight in enumerate(insights_data):
            with st.expander(f"{insight.get('title', 'Insight')} - {insight.get('severity', 'Info').upper()}"):
                st.write(f"**Description:** {insight.get('description', 'N/A')}")
                st.write(f"**Confidence:** {insight.get('confidence', 0):.0%}")
                st.write(f"**Recommendation:** {insight.get('recommendation', 'N/A')}")
                st.write(f"**Impact:** {insight.get('impact', 'N/A')}")
    else:
        st.info("Behavioral insights list will be displayed here.")

if __name__ == "__main__":
    main()

