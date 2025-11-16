# 🔥 DNR Priority Landscape Burn Projection Dashboard

This repository now hosts an interactive Streamlit application for exploring FSim summaries and calculating the weighted burn rate (percent of acres burned) for every Washington DNR Priority Landscape in Eastern Washington.

The dashboard lets analysts:

- Upload official FSim summary CSV/TSV exports.
- Automatically match rows to DNR plan areas and acreage.
- Calculate annual burn percentage / weighted burn rate from either `weighted_burn_rate`, `annual_burn_pct`, or `burned_acres` fields.
- Compare scenarios, filter by landscapes or years, visualize trajectories, and download aggregated tables.

## How to run it locally

1. Install the Python dependencies (Streamlit, pandas, Altair).

   ```bash
   pip install -r requirements.txt
   ```

2. Launch the Streamlit development server.

   ```bash
   streamlit run streamlit_app.py
   ```

3. In the sidebar choose whether to upload your FSim summary or explore with the built‑in synthetic sample dataset. To compute FSim weighted burn rates for each priority landscape ensure your file includes:

   | Column | Purpose |
   | --- | --- |
   | `plan_area` *(or `landscape`, `priority_landscape`, etc.)* | DNR Priority Landscape name. |
   | `year` | Simulation / observed year. |
   | `scenario` *(optional)* | Scenario label, e.g., "2050 climate". |
   | `weighted_burn_rate`, `annual_burn_pct`, or `burned_acres` | The app will compute percentages automatically. For FSim weighted burn rates expressed as 0–1 probabilities, they are scaled to percentages internally. |
   | `acres` *(optional)* | If omitted, the dashboard uses the official acreage list bundled with the app. |

4. Adjust the filters to see per‑landscape burn trajectories. The aggregated table can be downloaded for further analysis.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blank-app-template.streamlit.app/)
