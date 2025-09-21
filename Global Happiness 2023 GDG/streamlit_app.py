import streamlit as st
import pickle
import pandas as pd


with open("final_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("training_columns_2023.pkl", "rb") as f:
    columns = pickle.load(f)  # training feature names

st.set_page_config(page_title="Happiness Predictor", page_icon="🌍", layout="wide")

st.title("🌍 Global Happiness Predictor")
st.markdown("Predict or compare **Happiness Scores** based on world factors.")

# Prefill values for Sub-Saharan Africa (averages from dataset)
SUB_SAHARAN_DEFAULTS = {
    "gdp_per_capita": 0.7,
    "healthy_life_expectancy": 0.5,
    "freedom_to_make_life_choices": 0.45,
    "social_support": 0.8,
    "generosity": 0.2,
    "perceptions_of_corruption": 0.85,
    "year": 2020,
    "region": "Sub-Saharan Africa",
}



# Explanation helper
def explain_prediction(input_df):
    explanations = []
    row = input_df.iloc[0]  # single input row

    if "gdp_per_capita" in row:
        if row["gdp_per_capita"] < 0.6:
            explanations.append("💰 Low GDP per capita may reduce happiness.")
        else:
            explanations.append("💰 Higher GDP per capita contributes positively.")

    if "healthy_life_expectancy" in row:
        if row["healthy_life_expectancy"] < 0.6:
            explanations.append("🏥 Shorter healthy life expectancy lowers happiness.")
        else:
            explanations.append("🏥 Longer healthy life expectancy boosts happiness.")

    if "freedom_to_make_life_choices" in row:
        if row["freedom_to_make_life_choices"] < 0.4:
            explanations.append("🗽 Limited freedom reduces well-being.")
        else:
            explanations.append("🗽 Strong freedom of choice increases well-being.")

    if "social_support" in row:
        if row["social_support"] < 0.6:
            explanations.append("👥 Weak social support lowers happiness.")
        else:
            explanations.append("👥 Strong social support increases happiness.")

    if "generosity" in row:
        if row["generosity"] < 0.2:
            explanations.append("🎁 Low generosity has little positive impact.")
        else:
            explanations.append("🎁 High generosity supports social trust.")

    if "perceptions_of_corruption" in row:
        if row["perceptions_of_corruption"] > 0.7:
            explanations.append("⚖️ High corruption perception reduces happiness.")
        else:
            explanations.append("⚖️ Lower corruption perception supports happiness.")

    return explanations



# Input Form Function
def get_inputs(prefix="", defaults=None):
    st.subheader(f"{prefix} Inputs")
    col1, col2 = st.columns(2)
    input_data = {}

    defaults = defaults or {}

    with col1:
        if "gdp_per_capita" in columns:
            input_data["gdp_per_capita"] = st.number_input(
                f"{prefix} 💰 GDP per capita",
                min_value=0.0,
                max_value=2.0,
                value=defaults.get("gdp_per_capita", 1.0),
                step=0.01,
            )

        if "healthy_life_expectancy" in columns:
            input_data["healthy_life_expectancy"] = st.number_input(
                f"{prefix} 🏥 Healthy life expectancy",
                min_value=0.0,
                max_value=1.5,
                value=defaults.get("healthy_life_expectancy", 0.8),
                step=0.01,
            )

        if "freedom_to_make_life_choices" in columns:
            input_data["freedom_to_make_life_choices"] = st.number_input(
                f"{prefix} 🗽 Freedom of choice",
                min_value=0.0,
                max_value=1.0,
                value=defaults.get("freedom_to_make_life_choices", 0.5),
                step=0.01,
            )

    with col2:
        if "social_support" in columns:
            input_data["social_support"] = st.number_input(
                f"{prefix} 👥 Social support",
                min_value=0.0,
                max_value=1.5,
                value=defaults.get("social_support", 1.0),
                step=0.01,
            )

        if "generosity" in columns:
            input_data["generosity"] = st.number_input(
                f"{prefix} 🎁 Generosity",
                min_value=0.0,
                max_value=1.0,
                value=defaults.get("generosity", 0.2),
                step=0.01,
            )

        if "perceptions_of_corruption" in columns:
            input_data["perceptions_of_corruption"] = st.number_input(
                f"{prefix} ⚖️ Corruption",
                min_value=0.0,
                max_value=1.0,
                value=defaults.get("perceptions_of_corruption", 0.3),
                step=0.01,
            )

    region_cols = [c for c in columns if c.startswith("region_")]
    if region_cols:
        regions = [c.replace("region_", "") for c in region_cols]
        default_region = defaults.get("region", regions[0])
        selected_region = st.selectbox(f"{prefix} 🌎 Region", regions, index=regions.index(default_region))

        for col in region_cols:
            input_data[col] = 1 if col == f"region_{selected_region}" else 0

    if "year" in columns:
        input_data["year"] = st.slider(
            f"{prefix} 📅 Year",
            min_value=2015,
            max_value=2023,
            step=1,
            value=defaults.get("year", 2020),
        )

    return pd.DataFrame([input_data], columns=columns)


# Main UI

compare_mode = st.checkbox("🔄 Compare Two Scenarios")

if compare_mode:
    colA, colB = st.columns(2)
    with colA:
        df1 = get_inputs("Scenario A", defaults=SUB_SAHARAN_DEFAULTS)
    with colB:
        df2 = get_inputs("Scenario B")

    if st.button("🔮 Compare Predictions"):
        pred1 = model.predict(df1)[0]
        pred2 = model.predict(df2)[0]

        st.success(f"🌟 Scenario A Happiness Score: **{pred1:.2f}**")
        for exp in explain_prediction(df1):
            st.write(exp)

        st.success(f"🌟 Scenario B Happiness Score: **{pred2:.2f}**")
        for exp in explain_prediction(df2):
            st.write(exp)

        diff = pred2 - pred1
        if diff > 0:
            st.info(f"📈 Scenario B is **{diff:.2f} points happier** than Scenario A")
        elif diff < 0:
            st.warning(f"📉 Scenario A is **{abs(diff):.2f} points happier** than Scenario B")
        else:
            st.write("⚖️ Both scenarios have the **same predicted happiness**.")

else:
    df = get_inputs("Single Prediction")
    if st.button("🔮 Predict"):
        pred = model.predict(df)[0]
        st.success(f"🌟 Predicted Happiness Score: **{pred:.2f}**")

        for exp in explain_prediction(df):
            st.write(exp)
