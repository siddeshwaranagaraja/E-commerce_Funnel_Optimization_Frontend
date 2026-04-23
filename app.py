import streamlit as st
import pages.funnel_overview
import pages.dropoff_analysis
import pages.behavior_insights
import pages.experiments
import pages.recommendations

st.set_page_config(
    page_title="E-commerce Funnel Optimization",
    page_icon="📈",
    layout="wide",
)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Funnel Overview", "Drop-off Analysis", "Behavior Insights", "Experiments", "Recommendations"]
)

if page == "Funnel Overview":
    pages.funnel_overview.main()
elif page == "Drop-off Analysis":
    pages.dropoff_analysis.main()
elif page == "Behavior Insights":
    pages.behavior_insights.main()
elif page == "Experiments":
    pages.experiments.main()
elif page == "Recommendations":
    pages.recommendations.main()

st.title("E-commerce Funnel Optimization & Experimentation Engine")
st.write("Frontend entry point placeholder for funnel analysis, drop-off insights, and optimization recommendations.")

st.info("Navigation and sidebar placeholders are configured here.")
