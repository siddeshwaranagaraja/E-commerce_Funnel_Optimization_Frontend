# E-commerce Funnel Optimization Frontend

## Setup

- Install dependencies: `pip install -r requirements.txt`
- Run the app locally: `streamlit run app.py`

## Backend Connection

- Configure the backend base URL in `frontend/config/settings.py`
- Use `python-dotenv` to manage local environment variables if needed

## Pages

- **Funnel Overview** (`pages/funnel_overview.py`) - Displays conversion funnel metrics, key KPIs, and trend analysis
- **Drop-off Analysis** (`pages/dropoff_analysis.py`) - Shows drop-off points, stage-by-stage breakdown, and device analysis
- **Behavior Insights** (`pages/behavior_insights.py`) - User journey patterns, session duration, and product interactions
- **Experiments** (`pages/experiments.py`) - A/B testing experiments, results, and AI-suggested tests
- **Recommendations** (`pages/recommendations.py`) - UX improvements, conversion optimization, and priority actions

## Notes

- This frontend is the Streamlit entry point for funnel analysis, drop-off tracking, experimentation ideas, and optimization recommendations.
