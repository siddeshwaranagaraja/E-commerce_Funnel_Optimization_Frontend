import streamlit as st
from services import api_client

def main():
    st.set_page_title("Drop-off Analysis")

    st.title("📉 Drop-off Analysis")

    # Sidebar filter placeholder
    st.sidebar.header("Filters")
    date_range = st.sidebar.selectbox("Date Range", ["Last 7 days", "Last 30 days", "Last 90 days"])
    device_filter = st.sidebar.multiselect("Device", ["All", "Mobile", "Desktop", "Tablet"], default="All")

    # Build filters dict for API calls
    filters = {
        "date_range": date_range,
        "device": device_filter
    }

    # Fetch dropoff summary and stage leakage data
    dropoff_data = api_client.get_dropoff_summary(filters=filters)
    leakage_data = api_client.get_stage_leakage(filters=filters)

    # Stage comparison chart placeholder
    # Layout: bar chart comparing drop-off rates across stages
    # Components: render_dropoff_chart(data)
    st.subheader("Drop-off Points")
    if dropoff_data:
        st.json(dropoff_data)  # Placeholder display
    else:
        st.info("Stage comparison chart will be displayed here.")

    # Drop-off table placeholder
    # Layout: data table with stage, from_count, to_count, dropoff_rate columns
    # Components: render_stage_comparison_table(data)
    st.subheader("Drop-off by Stage")
    if leakage_data:
        st.json(leakage_data)  # Placeholder display
    else:
        st.info("Drop-off table will be displayed here.")

    # Segment filter layout placeholder
    # Layout: filterable view by device, time period, user segment
    st.subheader("Device Analysis")
    st.info("Device segment filter and analysis will be displayed here.")

if __name__ == "__main__":
    main()
