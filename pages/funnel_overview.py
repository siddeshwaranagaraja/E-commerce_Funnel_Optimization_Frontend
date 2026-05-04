import streamlit as st
from services import api_client

def main():
    st.set_page_title("Funnel Overview")

    st.title("📊 Funnel Overview")

    # Sidebar filter placeholder
    st.sidebar.header("Filters")
    date_range = st.sidebar.selectbox("Date Range", ["Last 7 days", "Last 30 days", "Last 90 days"])
    device_filter = st.sidebar.multiselect("Device", ["All", "Mobile", "Desktop", "Tablet"], default="All")

    # Build filters dict for API calls
    filters = {
        "date_range": date_range,
        "device": device_filter
    }

    # Fetch conversion summary data for KPIs
    conversion_data = api_client.get_conversion_summary(filters=filters)

    # Top KPIs placeholder
    # Layout: row of 4-5 metric cards (browse, cart, checkout, purchase, conversion rate)
    # Components: render_browse_count(), render_cart_count(), render_checkout_count(), render_purchase_count(), render_overall_conversion()
    st.subheader("Key Metrics")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    if conversion_data:
        with col1:
            st.metric("Browse Count", conversion_data.get("browse_count", 0))
        with col2:
            st.metric("Cart Count", conversion_data.get("cart_count", 0))
        with col3:
            st.metric("Checkout Count", conversion_data.get("checkout_count", 0))
        with col4:
            st.metric("Purchase Count", conversion_data.get("purchase_count", 0))
        with col5:
            conversion_rate = conversion_data.get("overall_conversion", 0)
            st.metric("Conversion Rate", f"{conversion_rate:.2f}%")
    else:
        with col1:
            st.info("Browse count placeholder")
        with col2:
            st.info("Cart count placeholder")
        with col3:
            st.info("Checkout count placeholder")
        with col4:
            st.info("Purchase count placeholder")
        with col5:
            st.info("Conversion rate placeholder")

    # Fetch funnel summary data for funnel chart
    funnel_data = api_client.get_funnel_summary(filters=filters)

    # Funnel chart placeholder
    # Layout: full-width funnel visualization
    # Components: render_funnel_chart(data)
    st.subheader("Conversion Funnel")
    if funnel_data:
        st.json(funnel_data)  # Placeholder display
    else:
        st.info("Funnel chart will be displayed here.")

    # Fetch trend data for trend chart
    trend_data = api_client.get_trend_data(filters=filters)

    # Trend chart placeholder
    # Layout: time-series line chart with multiple metrics
    # Components: render_trend_chart(data, x_col='date', y_col='count')
    st.subheader("Trend Analysis")
    if trend_data:
        st.json(trend_data)  # Placeholder display
    else:
        st.info("Trend chart will be displayed here.")

if __name__ == "__main__":
    main()
