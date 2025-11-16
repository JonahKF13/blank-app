from typing import Dict, List

import altair as alt
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="DNR Priority Landscape Burn Projection Dashboard",
    page_icon="🔥",
    layout="wide",
)

st.title("🔥 DNR Priority Landscape Burn Projection Dashboard")
st.caption(
    "Interactively explore annual burn percentage projections derived from FSim summaries "
    "for the Washington Department of Natural Resources (DNR) Priority Landscapes in Eastern Washington."
)

PRIORITY_LANDSCAPES: List[Dict[str, object]] = [
    {"plan_area": "Ione", "plan_year": 2020, "acres": 44248.1369, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_ione_le_summary_final_2023.pdf"},
    {"plan_area": "Republic", "plan_year": 2020, "acres": 180552.6328, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_republic_le_summary_final_2023.pdf"},
    {"plan_area": "Long Lake", "plan_year": 2020, "acres": 103290.2524, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_long_lake_le_summary_final_2023.pdf"},
    {"plan_area": "Stemilt", "plan_year": 2018, "acres": 38960.67831, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_stemilt_squilchuck_le_summary_final.pdf"},
    {"plan_area": "Little Pend Oreille", "plan_year": 2022, "acres": 117820.3346, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_little_pend_orielle_le_summary_final_2022.pdf"},
    {"plan_area": "Klickitat", "plan_year": 2020, "acres": 149649.2998, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_klickitat_le_summary_final_2023.pdf"},
    {"plan_area": "Manastash Taneum", "plan_year": 2018, "acres": 104071.6814, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_manastash_taneum_le_summary_final.pdf"},
    {"plan_area": "HWY 97", "plan_year": 2022, "acres": 60397.07242, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_highway_97_le_summary_final_2022.pdf"},
    {"plan_area": "Trail", "plan_year": 2020, "acres": 105241.261, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_trail_le_summary_final_2023.pdf"},
    {"plan_area": "Glenwood", "plan_year": 2020, "acres": 104501.7078, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/glenwood_le_summary_final_2023.pdf"},
    {"plan_area": "Tillicum", "plan_year": 2018, "acres": 14326.3265, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_tilllicum_le_summary_final.pdf"},
    {"plan_area": "Touchet-Mill", "plan_year": 2022, "acres": 203745.4922, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_touchet_mill_le_summary_final_2022.pdf"},
    {"plan_area": "Twisp River", "plan_year": 2020, "acres": 111916.5141, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_2020_le_twisp_river.pdf"},
    {"plan_area": "Mission", "plan_year": 2018, "acres": 49120.87849, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_mission_maintenance_summary_final.pdf"},
    {"plan_area": "Little White", "plan_year": 2020, "acres": 95749.94363, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_2020_le_little_white.pdf"},
    {"plan_area": "Cle Elum", "plan_year": 2018, "acres": 109396.6492, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_2020_le_cle_elum.pdf"},
    {"plan_area": "Dollar", "plan_year": 2022, "acres": 61237.85661, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_dollar_le_summary_final_2022.pdf"},
    {"plan_area": "Mad Roaring Mills", "plan_year": 2020, "acres": 65008.14835, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_mad_roaring_mills_le_summary_final_2023.pdf"},
    {"plan_area": "Chumstick to LP", "plan_year": 2020, "acres": 115333.773, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_2020_le_chumstick_lp.pdf"},
    {"plan_area": "White Salmon", "plan_year": 2018, "acres": 126688.6265, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_white_salmon_le_summary_final_24.pdf"},
    {"plan_area": "Mill Creek", "plan_year": 2018, "acres": 186306.2109, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_mill_creek_le_summary_final.pdf"},
    {"plan_area": "Upper Swauk", "plan_year": 2020, "acres": 39174.54251, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_2020_le_upper_swauk.pdf"},
    {"plan_area": "Tieton", "plan_year": 2020, "acres": 148634.1601, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_2020_le_tieton.pdf"},
    {"plan_area": "Teanaway", "plan_year": 2020, "acres": 132119.2567, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_2020_le_teanaway.pdf"},
    {"plan_area": "Mt Spokane", "plan_year": 2022, "acres": 121766.7853, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_mt_spokane_le_summary_final_2022.pdf"},
    {"plan_area": "Chelan", "plan_year": 2022, "acres": 98050.75136, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_chelan_le_summary_final_2022.pdf"},
    {"plan_area": "Deer Park", "plan_year": 2022, "acres": 181171.1239, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_deer_park_le_summary_final_2022.pdf"},
    {"plan_area": "Toroda-Tonata", "plan_year": 2020, "acres": 153611.9594, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_toroda_tonata_le_summary_final_2023.pdf"},
    {"plan_area": "Mt Hull", "plan_year": 2020, "acres": 105431.0884, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_mt_hull_le_summary_final_2023.pdf"},
    {"plan_area": "Trout Lake", "plan_year": 2018, "acres": 117152.715, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_trout_lake_le_summary_final.pdf"},
    {"plan_area": "Chewelah", "plan_year": 2018, "acres": 195407.6018, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/chewelah_le_summary_final_2023.pdf"},
    {"plan_area": "Ahtanum", "plan_year": 2018, "acres": 120478.412, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_ahtanum_le_summary_final.pdf"},
    {"plan_area": "Nason Creek", "plan_year": 2020, "acres": 31679.07814, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_2020_le_nason_creek.pdf"},
    {"plan_area": "Little Naches", "plan_year": 2022, "acres": 95432.67869, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_little_naches_le_summary_final_2022.pdf"},
    {"plan_area": "Upper Wenatchee", "plan_year": 2018, "acres": 74777.20524, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_upper_wenatchee_le_summary_final.pdf"},
    {"plan_area": "Stranger", "plan_year": 2020, "acres": 89904.08814, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_stranger_le_summary_final_2023.pdf"},
    {"plan_area": "Methow Valley", "plan_year": 2020, "acres": 338245.3802, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_2020_le_methow.pdf"},
    {"plan_area": "Asotin", "plan_year": 2026, "acres": 149151.4219, "fact_sheet": "coming soon"},
    {"plan_area": "Chewuch", "plan_year": 2024, "acres": 94250.39239, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_chewuch_le_summary_2024.pdf"},
    {"plan_area": "Gifford", "plan_year": 2024, "acres": 71961.51344, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_gifford_le_summary_2024.pdf"},
    {"plan_area": "Inchelium", "plan_year": 2024, "acres": 146262.6405, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_inchelium_le_summary_2024.pdf"},
    {"plan_area": "Loomis", "plan_year": 2024, "acres": 198991.1328, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_loomis_le_summary_2024.pdf"},
    {"plan_area": "Meadow", "plan_year": 2024, "acres": 60234.23241, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_meadow_le_summary_2024.pdf"},
    {"plan_area": "Mica", "plan_year": 2024, "acres": 72607.53155, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_mica_le_summary_2024.pdf"},
    {"plan_area": "Naches-Wenas", "plan_year": 2024, "acres": 180858.3448, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_naches_wenas_le_summary_2024.pdf"},
    {"plan_area": "Slate", "plan_year": 2024, "acres": 35947.52739, "fact_sheet": "https://www.dnr.wa.gov/sites/default/files/publications/rp_slate_le_summary_2024.pdf"},
    {"plan_area": "Tucannon", "plan_year": 2026, "acres": 98614.83869, "fact_sheet": "coming soon"},
    {"plan_area": "Conconully", "plan_year": 2026, "acres": 198243, "fact_sheet": "coming soon"},
    {"plan_area": "Curlew", "plan_year": 2026, "acres": 113401, "fact_sheet": "coming soon"},
    {"plan_area": "Entiat", "plan_year": 2026, "acres": 80936, "fact_sheet": "coming soon"},
    {"plan_area": "Kettle", "plan_year": 2026, "acres": 58330, "fact_sheet": "coming soon"},
    {"plan_area": "Orient", "plan_year": 2026, "acres": 82590, "fact_sheet": "coming soon"},
    {"plan_area": "Spokane North", "plan_year": 2026, "acres": 51656, "fact_sheet": "coming soon"},
    {"plan_area": "Upper Yakima", "plan_year": 2026, "acres": 98825, "fact_sheet": "coming soon"},
    {"plan_area": "Usk", "plan_year": 2026, "acres": 65477, "fact_sheet": "coming soon"},
]


@st.cache_data(show_spinner=False)
def load_priority_landscapes() -> pd.DataFrame:
    return pd.DataFrame(PRIORITY_LANDSCAPES)


@st.cache_data(show_spinner=False)
def load_sample_fsim(landscapes: pd.DataFrame) -> pd.DataFrame:
    """Create a small synthetic FSim summary so the UI works without a file."""

    records: List[Dict[str, float]] = []
    scenario_adjustments = {
        "Observed weather": 0.0,
        "2035 climate": 0.25,
        "2050 climate": 0.55,
    }

    for idx, (_, row) in enumerate(landscapes.iterrows()):
        base_pct = 0.15 + (idx % 6) * 0.08
        for scenario, scenario_adjust in scenario_adjustments.items():
            for year in range(2016, 2025):
                trend = 0.03 * (year - 2016)
                pct = min(max(base_pct + trend + scenario_adjust, 0.05), 8.0)
                burned_acres = pct / 100 * row.acres
                records.append(
                    {
                        "plan_area": row.plan_area,
                        "year": year,
                        "scenario": scenario,
                        "annual_burn_pct": round(pct, 3),
                        "burned_acres": round(burned_acres, 2),
                    }
                )
    return pd.DataFrame.from_records(records)


def _rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    rename_map = {
        "landscape": "plan_area",
        "priority_landscape": "plan_area",
        "planarea": "plan_area",
        "plan": "plan_area",
        "fire_year": "year",
        "simulation_year": "year",
        "scenario_name": "scenario",
        "weather_scenario": "scenario",
        "burn_perc": "annual_burn_pct",
        "burn_percent": "annual_burn_pct",
        "burn_pct": "annual_burn_pct",
        "burn_probability": "annual_burn_pct",
        "burned_percent": "annual_burn_pct",
        "burned_percentage": "annual_burn_pct",
        "burned_acre": "burned_acres",
        "annual_burn_percent": "annual_burn_pct",
        "weighted_burn_rate": "annual_burn_pct",
        "weighted_burnrate": "annual_burn_pct",
        "weighted_burn_pct": "annual_burn_pct",
        "weightedburnrate": "annual_burn_pct",
    }
    cleaned = df.rename(columns={c: rename_map.get(c.lower(), c.lower()) for c in df.columns})
    return cleaned


def prepare_fsim_dataset(raw_df: pd.DataFrame, landscapes: pd.DataFrame) -> pd.DataFrame:
    df = raw_df.copy()
    df.columns = [col.strip() for col in df.columns]
    df = _rename_columns(df)

    if "plan_area" not in df.columns or "year" not in df.columns:
        raise ValueError("The dataset must include plan_area and year columns.")

    df["plan_area"] = df["plan_area"].astype(str).str.strip()
    df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")

    if "scenario" not in df.columns:
        df["scenario"] = "Not specified"

    df = df.merge(landscapes, on="plan_area", how="left", validate="m:1")
    missing_acres = df["acres"].isna().sum()
    if missing_acres:
        st.warning(
            f"{missing_acres} records reference landscapes that are not on the DNR list. "
            "They will appear with blank acre values."
        )

    if "annual_burn_pct" not in df.columns:
        if "burned_acres" in df.columns and "acres" in df.columns:
            df["annual_burn_pct"] = (df["burned_acres"] / df["acres"]) * 100
        else:
            raise ValueError(
                "The dataset must include either an annual_burn_pct column or burned_acres so the metric can be computed."
            )

    df["annual_burn_pct"] = pd.to_numeric(df["annual_burn_pct"], errors="coerce")

    # FSim weighted burn rates are often stored as decimals (0-1). If all non-null
    # values fall inside that range treat them as proportions and convert to pct.
    pct_mask = df["annual_burn_pct"].between(0, 1)
    if pct_mask.any() and pct_mask.all():
        df.loc[pct_mask, "annual_burn_pct"] = df.loc[pct_mask, "annual_burn_pct"] * 100

    df = df.dropna(subset=["year", "annual_burn_pct"])
    df = df.sort_values(["plan_area", "scenario", "year"])

    if "burned_acres" not in df.columns and "acres" in df.columns:
        df["burned_acres"] = (df["annual_burn_pct"] / 100) * df["acres"]

    df["change_vs_prev_year"] = (
        df.groupby(["plan_area", "scenario"])["annual_burn_pct"].diff()
    )
    return df


def add_baseline_columns(df: pd.DataFrame, baseline_year: int) -> pd.DataFrame:
    baseline = (
        df[df["year"] == baseline_year][["plan_area", "scenario", "annual_burn_pct"]]
        .rename(columns={"annual_burn_pct": "baseline_pct"})
    )
    df = df.merge(baseline, on=["plan_area", "scenario"], how="left")
    df["change_from_baseline"] = df["annual_burn_pct"] - df["baseline_pct"]
    return df


def summarize_landscapes(df: pd.DataFrame) -> pd.DataFrame:
    grouped = (
        df.sort_values("year")
        .groupby(["plan_area", "scenario"], as_index=False)
        .agg(
            acres=("acres", "first"),
            baseline_pct=("baseline_pct", "first"),
            latest_year=("year", "last"),
            latest_pct=("annual_burn_pct", "last"),
            change_from_baseline=("change_from_baseline", "last"),
            change_vs_prev_year=("change_vs_prev_year", "last"),
        )
    )
    grouped["baseline_pct"] = grouped["baseline_pct"].round(3)
    grouped["latest_pct"] = grouped["latest_pct"].round(3)
    grouped["change_from_baseline"] = grouped["change_from_baseline"].round(3)
    grouped["change_vs_prev_year"] = grouped["change_vs_prev_year"].round(3)
    return grouped


landscapes_df = load_priority_landscapes()

with st.sidebar:
    st.header("1. Provide FSim results")
    uploaded_file = st.file_uploader(
        "Upload an FSim summary (CSV or TSV)", type=["csv", "tsv"], accept_multiple_files=False
    )
    use_sample = st.toggle(
        "Use built-in sample FSim data",
        value=uploaded_file is None,
        help="Enable this if you want to explore the dashboard without uploading a file.",
    )

if uploaded_file is not None:
    try:
        delimiter = "," if uploaded_file.name.endswith(".csv") else "\t"
        fsim_raw = pd.read_csv(uploaded_file, delimiter=delimiter)
        data_source_label = f"Uploaded file: {uploaded_file.name}"
    except Exception as exc:  # pragma: no cover - defensive UI guard
        st.error(f"Could not read the uploaded file: {exc}")
        st.stop()
elif use_sample:
    fsim_raw = load_sample_fsim(landscapes_df)
    data_source_label = "Synthetic sample derived from acreage list"
else:
    st.info("Upload a file or enable the sample dataset to continue.")
    st.stop()

try:
    fsim_df = prepare_fsim_dataset(fsim_raw, landscapes_df)
except ValueError as exc:
    st.error(str(exc))
    st.stop()

available_years = sorted(fsim_df["year"].dropna().unique())
if not available_years:
    st.warning("No valid simulation years were found in the dataset.")
    st.stop()

with st.sidebar:
    st.header("2. Configure the analysis")
    scenario_options = sorted(fsim_df["scenario"].unique())
    scenario_selection = st.multiselect(
        "Scenario(s)", options=scenario_options, default=scenario_options
    )

    landscape_options = sorted(fsim_df["plan_area"].unique())
    default_selection = [name for name in ["Methow Valley", "Chelan", "Klickitat"] if name in landscape_options]
    if not default_selection and landscape_options:
        default_selection = landscape_options[: min(5, len(landscape_options))]

    landscape_selection = st.multiselect(
        "Priority landscapes",
        options=landscape_options,
        default=default_selection,
        help="Hold shift or command/control to pick multiple areas.",
    )

    min_year, max_year = int(available_years[0]), int(available_years[-1])
    selected_year_range = st.slider(
        "Simulation year range",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year),
    )

    baseline_year = st.selectbox(
        "Baseline year for percent-change calculations",
        options=available_years,
        index=0,
        help="All percent changes will be computed relative to this year when data are available.",
    )

filtered_df = fsim_df.copy()
filtered_df = filtered_df[filtered_df["scenario"].isin(scenario_selection)]
if landscape_selection:
    filtered_df = filtered_df[filtered_df["plan_area"].isin(landscape_selection)]
filtered_df = filtered_df[
    (filtered_df["year"] >= selected_year_range[0]) & (filtered_df["year"] <= selected_year_range[1])
]

filtered_df = add_baseline_columns(filtered_df, baseline_year)

if filtered_df.empty:
    st.warning("No records match the selected filters.")
    st.stop()

summary_df = summarize_landscapes(filtered_df)

st.subheader("Annual burn percentage summary")
left_col, right_col, third_col = st.columns(3)
mean_latest_pct = summary_df["latest_pct"].mean()
mean_change_baseline = summary_df["change_from_baseline"].mean()
mean_yoy_change = summary_df["change_vs_prev_year"].mean()

left_col.metric("Avg. latest annual burn %", f"{mean_latest_pct:0.2f}%")
right_col.metric("Avg. change vs. baseline", f"{mean_change_baseline:0.2f} pct pts")
third_col.metric(
    "Avg. change vs. prior year", f"{mean_yoy_change:0.2f} pct pts",
    help="Difference between the most recent year and the previous year, averaged across selected landscapes.",
)

st.write(f"**Data source:** {data_source_label}")
st.dataframe(
    summary_df,
    width="stretch",
    hide_index=True,
)

chart_data = filtered_df.dropna(subset=["annual_burn_pct"])  # keep clean for charting

if not chart_data.empty:
    line_chart = (
        alt.Chart(chart_data)
        .mark_line(point=True)
        .encode(
            x=alt.X("year:O", title="Simulation year"),
            y=alt.Y("annual_burn_pct:Q", title="Annual burn percentage"),
            color=alt.Color("plan_area", title="Priority landscape"),
            strokeDash="scenario",
            tooltip=["plan_area", "scenario", "year", alt.Tooltip("annual_burn_pct", title="Annual burn %", format=".2f"), alt.Tooltip("change_from_baseline", title="Δ vs baseline", format="+.2f")],
        )
        .properties(height=420)
    )
    st.subheader("Annual burn % trajectory")
    st.altair_chart(line_chart, width="stretch")
else:
    st.info("There are no rows with non-null annual burn percentages to plot.")

st.subheader("Download the aggregated table")
st.download_button(
    label="Download CSV",
    data=summary_df.to_csv(index=False).encode("utf-8"),
    file_name="dnr_priority_landscape_burn_summary.csv",
    mime="text/csv",
)

with st.expander("What format should my FSim data use?"):
    st.markdown(
        """
        Your file should include at least these fields:

        | Column | Description |
        | --- | --- |
        | `plan_area` | Name that matches one of the DNR priority landscapes. |
        | `year` | Simulation or observed year (numeric). |
        | `scenario` *(optional)* | Weather/climate scenario description. |
        | `annual_burn_pct` **or** `burned_acres` | Use whichever metric comes out of FSim. If you only have burned acres the app will compute the percentage using the acreage list above. |

        Additional columns such as ignition density, risk class, or modeled treatments can be present—they will be ignored during processing.
        """
    )

st.subheader("Reference: DNR Priority Landscapes")
st.dataframe(landscapes_df, width="stretch", hide_index=True)

st.caption(
    "The sample FSim dataset is synthetic and exists purely to demonstrate the workflow. "
    "Replace it with your official modeled results before sharing insights."
)
